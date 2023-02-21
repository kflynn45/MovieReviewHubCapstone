'''
Author: Connor Oaks
Date: 02-20-2023

This command was created in anticipation that IMDb data validation/filtering settings may change,
and provides an easy way to delete ImdbTitle objects from the database that were previously pulled in but no longer 
pass validation.

Intended to be run manually after a change has been made to validation related settings. 
'''


from django.core.management.base import BaseCommand
from mysite import settings
from mysite.models import ImdbTitle
import time 
import datetime


'''
Remove any saved titles that no longer pass validation 
'''
def cleanup():
    removed, objects = ImdbTitle.objects.exclude(
        votes__gte=settings.IMDB_TITLE_MINIMUM_VOTES,
        title_type__in=settings.IMDB_TITLE_TYPES
    ).delete()
    return removed 


class Command(BaseCommand): 
    def handle(self, *args, **options):
        time_elapsed = lambda t: str(datetime.timedelta(seconds=round(time.perf_counter() - t)))
        print("Starting IMDb data cleanup.", flush=True)
        start = time.perf_counter()
        removed = cleanup()
        print(f"{removed} records removed in {time_elapsed(start)}.")
        