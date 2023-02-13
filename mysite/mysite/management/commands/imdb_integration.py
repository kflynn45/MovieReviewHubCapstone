'''
Author: Connor Oaks
Date: 02-12-2023

This file contains code for a custom manage.py command to pull in and processes the newest IMDb datasets.
Intended to be run once every 24 hours (interval at which IMDb refreshes data)
Specific scheduling implementation may be platform specific.
'''

from django.core.management.base import BaseCommand, CommandError
from mysite import settings
import os
import requests
import gzip
import csv 


'''
Download the newest version of the passed IMDb dataset and save to the server as media
'''
def download_current_dataset(filename): 
    response = requests.get(settings.IMDB_BASE_URL + filename)
    if response.status_code == 200:
        with open(os.path.join(settings.MEDIA_ROOT, 'datasets', filename), 'wb') as dataset:
            dataset.write(gzip.decompress(response.content))


'''
Parse current dataset and refresh database with current data.
Update entries for existing movies, insert new records if they don't already exist.
'''
def upsert(filename):
    with open(os.path.join(settings.MEDIA_ROOT, 'datasets', filename), 'r') as dataset:
        #for row in csv.reader(dataset, delimiter='\t'): 
        #TODO: Upsert IMDb data in the database once data modeling is complete
        print("parse " + filename)


'''
Custom manage.py command entry point
'''
class Command(BaseCommand): 
    def handle(self, *args, **options):
        for filename in settings.IMDB_DATASETS: 
            download_current_dataset(filename)
            upsert(filename)
            os.remove(os.path.join(settings.MEDIA_ROOT, 'datasets', filename))      # delete dataset file once update is complete





