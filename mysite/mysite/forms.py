"""
Author: Connor Oaks
Date: 04-05-2023

This file contains forms for user input on our site.
"""

from django import forms

"""
Search bar on homepage
"""
class SearchForm(forms.Form): 
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'text-search', 
        'placeholder': 'Search...'
    }))