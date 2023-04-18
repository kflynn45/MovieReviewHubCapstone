"""
author: Connor Oaks
date: 04-17-2023

This file contains the server side logic for the title grid display.  
"""

from django.template.loader import render_to_string
from django.http import HttpResponseServerError, JsonResponse
from mysite import settings
from mysite.models import TitleGridSetting
import json
import requests


class TitleGrid: 

    def __init__(self, action, **kwargs):
        if 'page' not in kwargs: 
            kwargs['page'] = 1 

        data = self.get_titles(action, kwargs)

        self.titles = self.create_title_displays(data.json())
        self.action = action
        self.page = kwargs['page']
        self.show_pages = action not in ['search', 'recommended']
        
        try: 
            pager_setting = TitleGridSetting.objects.get(setting='page selector location')
            self.pager_location = pager_setting.value
            if self.pager_location != 'top' and self.pager_location != 'bottom':
                self.pager_location = settings.DEFAULT_PAGER_POSITION
        except: 
            self.pager_location = settings.DEFAULT_PAGER_POSITION
        


    """
    Call the appropriate TMDB API to fetch titles
    """
    def get_titles(self, action, url_params): 
        url = settings.MOVIE_GRID_URLS[action]
        url_params['apikey'] = settings.TMDB_API_KEY
        movie_data = requests.get(url.format(**url_params))
        if movie_data.status_code != 200: 
            raise HttpResponseServerError()
        
        return movie_data


    """
    Create objects for display and package them into rows for the template. 
    """
    def create_title_displays(self, response):
        try: 
            setting = TitleGridSetting.objects.get(setting='titles per row')
            step = int(setting.value)
        except: 
            step = settings.DEFAULT_TITLES_PER_ROW

        displays = list(map(lambda t: {
            'title_id': t['id'],
            'title': t['title'], 
            'poster': None if not t['poster_path'] else settings.TMDB_IMAGE_URL + t['poster_path']
        }, response['results']))

        return [displays[i:i+step] for i in range(0, len(displays), step)]



"""
Refresh the data and rerender the title grid display, then send the raw html back in a JSON object.
This is used for pagination, see 'page-selector.html'
"""
def refresh_titles(request): 
    data = json.loads(request.POST.get('url_params'))
    grid = render_to_string('grid-display.html', {
        'title_grid': TitleGrid(**data), 
    })
    return JsonResponse({
        'title_grid_html': grid
    }, status=200)
    
    
