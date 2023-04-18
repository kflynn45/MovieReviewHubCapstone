'''
Author: Connor Oaks
Date: 02-13-2023

This file contains the data models for this project. 
'''

from django.db import models


class TitleGridSetting(models.Model): 
    setting = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.setting