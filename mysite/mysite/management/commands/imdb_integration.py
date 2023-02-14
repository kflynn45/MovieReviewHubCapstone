'''
Author: Connor Oaks
Date: 02-12-2023

This file contains code for a custom manage.py command to pull in and processes the newest IMDb datasets.
Intended to be run once every 24 hours (interval at which IMDb refreshes data)
Specific scheduling implementation may be platform specific.
'''

from django.core.management.base import BaseCommand, CommandError
from mysite import settings
from mysite.models import ImdbTitle
import os
import requests
import gzip
import csv 
import time 
import datetime


'''
Download the newest version of the passed IMDb dataset and save to the server as media
'''
def download_current_dataset(filename): 
    response = requests.get(settings.IMDB_BASE_URL + filename)
    if response.status_code == 200:
        with open(os.path.join(settings.MEDIA_ROOT, 'datasets', filename), 'wb') as dataset:
            dataset.write(gzip.decompress(response.content))
    else:
        cleanup_dataset_files()
        raise CommandError(f"Unable to download current version of {filename}.")



'''
Open all dataset files and prepare for parsing
'''
def open_datasets():
    datasets = []
    for ds_info in settings.IMDB_DATASETS: 
        file = open(os.path.join(settings.MEDIA_ROOT, 'datasets', ds_info['internal_filename']), 'r', encoding='utf8')
        reader = csv.reader(file, delimiter='\t')
        column_header = next(reader)

        datasets.append({
            'file_handle': file,
            'dataset': reader, 
            'dataset_fields': ds_info['tsv_fields'], 
            'database_fields': ds_info['db_fields'], 
            'field_count': len(ds_info['db_fields']), 
            'tsv_mapping': {
                field: column_header.index(field) for field in ds_info['tsv_fields']
            }
        })
    return datasets


'''
Close the file pointers created by open_datasets
'''
def close_datasets(ds):
    for dataset in ds: 
        dataset['file_handle'].close() 


'''
Validate/filter data before entering into the database.
'''
def validate(row):
    #TODO: Discuss and implement filtering for data
    return True

'''
Parse current dataset and refresh database with current data.
Update entries for existing movies, insert new records if they don't already exist.
'''
def upsert():
    datasets = open_datasets()
    added, modified = 0, 0
    for x in range(100):               
        current_values = {}
        try: 
            for ds in datasets:
                row = next(ds['dataset'])
                for i in range(ds['field_count']):
                    current_values[ds['database_fields'][i]] = row[ds['tsv_mapping'][ds['dataset_fields'][i]]]
        except StopIteration: 
           break

        #print(current_values)
        if validate(current_values):
            title, created = ImdbTitle.objects.update_or_create(
                unique_id=current_values['unique_id'], 
                defaults=current_values
            )
            title.save()
            if created:
                added += 1
            else:
                modified += 1 

    close_datasets(datasets)
    return added, modified
    
    


'''
Delete all dataset files that exist on the server
'''
def cleanup_dataset_files(): 
    for dataset in settings.IMDB_DATASETS:
        ds_path = os.path.join(settings.MEDIA_ROOT, 'datasets', dataset['internal_filename'])
        if os.path.exists(ds_path):
            os.remove(ds_path)



'''
Custom manage.py command entry point
'''
class Command(BaseCommand): 
    def handle(self, *args, **options):
        start = time.perf_counter()
        for ds_info in settings.IMDB_DATASETS: 
            download_current_dataset(ds_info['external_filename'])
        finish = time.perf_counter()
        print(f"Successfully dowloaded IMDb datatsets in {str(datetime.timedelta(seconds=finish-start))}.")

        start = time.perf_counter()
        added, modified = upsert()
        finish = time.perf_counter()
        print(f"{added} records created, {modified} records updated in {str(datetime.timedelta(seconds=finish-start))}.")

        cleanup_dataset_files()





