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


class Home(View):
    """
    Process GET requests for the homepage. 
    """
    def get(self, request, action):
        if action not in settings.HOMEPAGE_MOVIE_GRID_OPTIONS: 
            raise Http404()
  
        return render(request, 'home.html', {
            'action': action, 
            'search_bar': SearchForm(), 
            'title_grid': TitleGrid(action), 
        })
    

    """
    Process POST requests for the homepage.
    """
    def post(self, request, action): 
        if action != 'search': 
            raise Http404()
        form = SearchForm(request.POST)
        if form.is_valid(): 
            search_query = form.cleaned_data['query']
            return render(request, 'home.html', {
                'search_bar': form, 
                'title_grid': TitleGrid('search', query=search_query), 
                'search': search_query
            })
        else:
            return render_error(request, 4)
            


        
