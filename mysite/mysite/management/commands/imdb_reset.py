'''
Author: Connor Oaks 
Date: 02-20-2023

Simpily remove all ImdbTitle objects from the database and delete any dataset files on the server. 
Meant to be run as needed or after imdb_integration fails. 
'''

from django.core.management.base import BaseCommand
from mysite import settings
from mysite.models import ImdbTitle
from mysite.management.commands import imdb_integration 
import time 
import datetime

class Command(BaseCommand): 
    def handle(self, *args, **options):
        time_elapsed = lambda t: str(datetime.timedelta(seconds=round(time.perf_counter() - t)))
        print("Starting IMDb data reset.", flush=True)
        start = time.perf_counter()
        removed, objects = ImdbTitle.objects.all().delete()
        imdb_integration.cleanup_dataset_files()
        print(f"Cleaned up dataset files and removed {removed} records in {time_elapsed(start)}.")