"""
Author: Connor Oaks
Date: 02-12-2023

This file contains code for a custom manage.py command to pull in and processes the newest IMDb ratings.
Intended to be run once every 24 hours (interval at which IMDb refreshes data)
Scheduling implementation may be platform specific.
"""

from django.core.management.base import BaseCommand, CommandError
from mysite import settings
from mysite.models import ImdbRating
import os
import requests
import gzip
import csv 
import time 
import datetime


"""
Download the latest IMDb ratings
"""
def download_current_dataset(): 
    response = requests.get(settings.IMDB_DATASET_URL)
    if response.status_code == 200:
        if not os.path.exists(settings.IMDB_DATASET_ROOT): 
            os.makedirs(settings.IMDB_DATASET_ROOT)
        with open(os.path.join(settings.IMDB_DATASET_ROOT, settings.IMDB_DATASET['filename']), 'wb') as dataset:
            dataset.write(gzip.decompress(response.content))
    else:
        raise CommandError("Unable to download current IMDb ratings.")


"""
Parse current ratings dataset and refresh database with current data.
Update entries for existing titles, insert new records if they don't already exist.
"""
def upsert_imdb_ratings():
    dataset_path = os.path.join(settings.IMDB_DATASET_ROOT, settings.IMDB_DATASET['filename'])
    with open(dataset_path, 'r', encoding='utf8') as ds_file: 
        dataset = csv.reader(ds_file, delimiter='\t')
        next(dataset)               # First row is column header

        ds_info = settings.IMDB_DATASET

        added, modified = 0, 0
        while True:                 # Loop until we run out of data                
            current_values = {}
            try: 
                row = next(dataset)
                current_values = {
                    ds_info['db_fields'][i]: row[i] for i in range(len(ds_info['db_fields']))
                }
            except StopIteration: 
                break

            object, created = ImdbRating.objects.update_or_create(
                unique_id=current_values['unique_id'], 
                defaults=current_values
            )
            if created:
                added += 1
            else:
                modified += 1 

    os.remove(dataset_path)
    return added, modified



class Command(BaseCommand): 
    def handle(self, *args, **options):
        time_elapsed = lambda t: str(datetime.timedelta(seconds=round(time.perf_counter() - t)))
        print("Starting IMDb data integration.", flush=True)

        start = time.perf_counter()
        download_current_dataset()
        print(f"Successfully dowloaded IMDb datatset in {time_elapsed(start)}.", flush=True)

        start = time.perf_counter()
        added, modified = upsert_imdb_ratings()
        print(f"{added} records created, {modified} records updated in {time_elapsed(start)}.")







