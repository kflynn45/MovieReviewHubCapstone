"""
Author: Connor Oaks
Date: 02-01-2023

This file contains the server side portion of the homepage.  
"""

from django.views import View
from django.shortcuts import render
from django.http import Http404
from mysite import settings
from mysite.forms import SearchForm
from mysite.models import TitleGridSetting
from mysite.views.error import render_error
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
        response = requests.get(url.format(apikey=settings.TMDB_API_KEY, page=grid_page))
        if response.status_code != 200: 
            return render_error(request, 2)
       
        return render(request, 'home.html', {
            'action': action, 
            'search_bar': SearchForm(), 
            'titles': get_title_displays(response.json()), 
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
                'titles': get_title_displays(response.json()), 
                'search': True 
            })
        else:
            return render_error(request, 4)
            



class TitleDisplay: 
    def __init__(self, title): 
        self.title_id = title['id']
        self.title = title['title']
        self.poster = None if not title['poster_path'] else settings.TMDB_IMAGE_URL + title['poster_path']


"""
Package JSON response data into TitleDisplay objects, 4 per row for the template
"""
def get_title_displays(response):
    try: 
        setting = TitleGridSetting.objects.get(setting='titles per row')
        step = int(setting.value)
    except: 
        step = settings.DEFAULT_TITLES_PER_ROW
    displays = list(map(TitleDisplay, response['results']))
    return [displays[i:i+step] for i in range(0, len(displays), step)]

        
