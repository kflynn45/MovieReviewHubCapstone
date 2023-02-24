'''
Author: Connor Oaks
Date: 02-13-2023

This file contains the data models for this project. 
'''

from django.db import models

class ImdbRating(models.Model): 
    unique_id = models.CharField(max_length=10)
    rating = models.DecimalField(decimal_places=1, max_digits=3, null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.unique_id} | {self.rating}"