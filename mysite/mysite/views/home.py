"""
Author: Connor Oaks
Date: 02-01-2023

This file contains the server side portion of the homepage.  
"""

from django.views import View
from django.shortcuts import render, redirect
from django.http import Http404
from mysite import settings
from mysite.forms import SearchForm
from mysite.views.error import render_error
from mysite.views.title_grid import TitleGrid
import requests



class Home(View):
    """
    Process GET requests for the homepage. 
    """
    def get(self, request, action, grid_page=1):
        try:
            url = settings.TMDB_MOVIE_GRID_URLS[action]
        except KeyError: 
            raise Http404()
        
        title_data = requests.get(url.format(
            apikey=settings.TMDB_API_KEY, 
            page=grid_page
        ))
        if title_data.status_code != 200:
            return render_error(request, 2)
  
        return render(request, 'home.html', {
            'action': action, 
            'search_bar': SearchForm(), 
            'title_grid': TitleGrid(title_data), 
            'page': grid_page 
        })
    

    """
    Process POST requests for the homepage.
    """
    def post(self, request, action): 
        if action != 'search': 
            raise Http404()
        form = SearchForm(request.POST)
        if form.is_valid(): 
            url = settings.TMDB_SEARCH_MOVIES_URL
            response = requests.get(url.format(
                apikey=settings.TMDB_API_KEY, 
                query=form.cleaned_data['query']
            ))
            if response.status_code != 200: 
                return render_error(request, 2)
            return render(request, 'home.html', {
                'search_bar': form, 
                'title_grid': TitleGrid(response), 
                'search': True 
            })
        else:
            return render_error(request, 4)
            


        
