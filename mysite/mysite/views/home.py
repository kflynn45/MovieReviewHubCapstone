"""
Author: Connor Oaks
Date: 02-01-2023

This file contains the server side portion of the homepage.  
"""

from django.views import View
from django.shortcuts import render, redirect
from mysite import settings
from mysite.forms import SearchForm
import requests



class Home(View):
    """
    Process GET requests for the homepage. 
    """
    def get(self, request, action):
        try:
            url = settings.TMDB_MOVIE_GRID_URLS[action]
        except KeyError: 
            pass #TODO error page  
        response = requests.get(url.format(apikey=settings.TMDB_API_KEY))
        if response.status_code != 200: 
            pass #TODO error page
       
        return render(request, 'home.html', {
            'search_form': SearchForm(), 
            'titles': get_title_displays(response.json()) 
        })
    

    """
    Process POST requests for the homepage.
    """
    def post(self, request, action): 
        if action != 'search': 
            pass #TODO error page
        form = SearchForm(request.POST)
        if form.is_valid(): 
            url = settings.TMDB_SEARCH_MOVIES_URL
            response = requests.get(url.format(
                apikey=settings.TMDB_API_KEY, 
                query=form.cleaned_data['query']
            ))
            if response.status_code != 200: 
                pass #TODO error page
            return render(request, 'home.html', {
                'search_form': form, 
                'titles': get_title_displays(response.json()), 
                'search': True 
            })
        else:
            pass #TODO error page
            



class TitleDisplay: 
    def __init__(self, title): 
        self.title_id = title['id']
        self.title = title['title']
        self.poster = None if not title['poster_path'] else settings.TMDB_IMAGE_URL + title['poster_path']


"""
Package JSON response data into TitleDisplay objects, 4 per row for the template
"""
def get_title_displays(response):
    displays = list(map(TitleDisplay, response['results']))
    return [displays[i:i+4] for i in range(0, len(displays), 4)]

        
