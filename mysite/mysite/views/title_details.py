"""
Author: Connor Oaks
Date: 02-22-2023

This file contains the view code for the title details page.  
"""

from django.views import View
from django.shortcuts import render
from mysite import settings
from mysite.models import ImdbRating
import requests

class TitleDetails(View):

    """
    Process get requests for the title details page.
    """
    def get(self, request, title_id):
        response = requests.get(settings.TMDB_GET_MOVIE_URL + f'{title_id}?api_key={settings.TMDB_API_KEY}&language=en_US')
        if(response.status_code != 200):
            pass #TODO: implement error landing page

        return render(request, 'title_details.html', {
            'title_info': TitleDetailInfo(**response.json())
        })



class TitleDetailInfo: 
    def get_imdb_score(self, imdb_id): 
        try: 
            rating_info = ImdbRating.objects.get(unique_id=imdb_id)
        except: 
            return "Unknown"
        return rating_info.rating
    
    def __init__(self, **title):
        self.title = title['title']
        self.description = title['overview']
        self.backdrop = settings.TMDB_IMAGE_URL + title['backdrop_path']
        self.poster = settings.TMDB_IMAGE_URL + title['poster_path']
        self.release_date = title['release_date']
        self.movie_db_rating = title['vote_average']
        self.movie_db_rating_count = title['vote_count']
        self.imdb_rating = self.get_imdb_score(title['imdb_id'])
        self.genres = title['genres']
        self.release_date = title['release_date']
