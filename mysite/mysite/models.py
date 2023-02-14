'''
Author: Connor Oaks
Date: 02-13-2023

This file contains the data models for this project. 
'''

from django.db import models

class ImdbTitle(models.Model): 
    unique_id = models.CharField(max_length=10)
    title_type = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    rating = models.DecimalField(decimal_places=1, max_digits=3)

    def __str__(self):
        return f"{self.title} | {self.release_year}"