"""
Author: Connor Oaks
Date: 02-22-2023

This file contains the view code for the title details page.  
"""

from django.views import View
from django.shortcuts import render, redirect
from mysite import settings
from mysite.models import ImdbRating
from mysite.views.error import render_error
from mysite.views.title_grid import TitleGrid
import requests
import bs4
import json


class TitleDetails(View):

    """
    Process get requests for the title details page.
    """
    def get(self, request, title_id):
        movie_details = requests.get(settings.TMDB_GET_MOVIE_URL.format(
            apikey=settings.TMDB_API_KEY, 
            movieid=title_id
        ))
        if movie_details.status_code != 200:
            return render_error(request, 2)
        
        tmdb_comments = requests.get(settings.TMDB_WRITTEN_REVIEWS_URL.format(
            apikey=settings.TMDB_API_KEY,
            movieid=title_id
        ))

        title_info = TitleDetailInfo(**movie_details.json())

        nyt_comments = requests.get(settings.NYT_API_URL.format(
            apikey=settings.NYT_API_KEY,
            query=title_info.title
        ))

        recommended = requests.get(settings.RECOMMENDED_URL.format(
            apikey=settings.TMDB_API_KEY, 
            movieid=title_id
        ))
        return render(request, 'title-details.html', {
            'title_info': title_info,
            'title_id': title_id,
            'tmdb_comments': tmdb_comments.json(),
            'nyt_comments': nyt_comments.json()
        })



class TitleDetailInfo:
    def __init__(self, **title):
        self.title = title['title']
        self.description = title['overview']
        self.backdrop = None if not title['backdrop_path'] else settings.TMDB_IMAGE_URL + title['backdrop_path']
        self.poster = None if not title['poster_path'] else settings.TMDB_IMAGE_URL + title['poster_path']
        self.release_date = title['release_date']
        self.movie_db_rating = title['vote_average']
        self.movie_db_rating_count = title['vote_count']
        self.imdb_rating = self.get_imdb_score(title['imdb_id'])
        self.genres = title['genres']
        self.release_date = title['release_date']
        self.movie_trailer = self.get_movie_trailer_video_url(title['imdb_id'])
        self.tmdb_rating = title['vote_average']
        self.movie_db_score_rotten = self.get_rotten_tomatoes_score(title['imdb_id'])
        self.movie_db_score_average = self.get_movie_average_score(title['imdb_id'])
        self.metacritic = self.get_metacritic_score(title['imdb_id'])


    def get_imdb_score(self, imdb_id):
        try:
            rotten_info_url = settings.ROTTEN_TOMATO_GET_MOVIE_URL + f'?apikey={settings.ROTTEN_TOMATO_API_KEY}&i={imdb_id}'
            response = requests.get(rotten_info_url)
            imdb_rating = response.json()['imdbRating']

            return imdb_rating

        except:
            return ""

    def get_rotten_tomatoes_score(self,imdb_id):
        try:
            rotten_info_url = settings.ROTTEN_TOMATO_GET_MOVIE_URL + f'?apikey={settings.ROTTEN_TOMATO_API_KEY}&i={imdb_id}'
            response = requests.get(rotten_info_url)
            rotten_tomatoes_score = ''

            for rating in response.json()['Ratings']:
                if rating['Source'] == 'Rotten Tomatoes':
                    rotten_tomatoes_score = rating['Value']

            if rotten_tomatoes_score == '':
                return ""

            return rotten_tomatoes_score

        except:
            return ""

    def get_movie_average_score(self,imdb_id):
        try:
            imdb_score = float(self.get_imdb_score(imdb_id)) * 10
            rotten_tomatoes_score = float(self.get_rotten_tomatoes_score(imdb_id).strip('%'))
            tmdb_score = float(self.tmdb_rating) * 10
            average_score = round((tmdb_score + rotten_tomatoes_score + imdb_score) / 3 , 2)

            return average_score

        except:
            return ""
        
    def get_metacritic_score(self,imdb_id):
        try:
            rotten_info_url = settings.ROTTEN_TOMATO_GET_MOVIE_URL + f'?apikey={settings.ROTTEN_TOMATO_API_KEY}&i={imdb_id}'
            response = requests.get(rotten_info_url)
            metacritic_score = response.json()['Metascore']

            return metacritic_score
        except:
            return ""

    def get_movie_trailer_url(self,imdb_id):
        try:
            imdb_trailerInfo_url = settings.IMDB_API_URL+'en/API/Trailer'+f'/{settings.IMDB_API_KEY}/{imdb_id}'
            response = requests.get(imdb_trailerInfo_url)
            movie_trailer_url = response.json()['linkEmbed']
            if movie_trailer_url:
                return movie_trailer_url
            return ""
        except:
            return "Cannot get trailer URL"
        
    def get_movie_trailer_video_url(self,imdb_id):
        try:
            movie_trailer_url = self.get_movie_trailer_url(imdb_id)
            response = requests.get(movie_trailer_url)
            soup = bs4.BeautifulSoup(response.text,'html.parser')
            videos_tag = soup.find(name="script", attrs={'class': 'imdb-player-data'}).getText('videoPlayerObject')
            videoInfoList = json.loads(videos_tag)["videoPlayerObject"]['video']['videoInfoList']
            videoUrl = ""
            for item in videoInfoList:
                if item['videoMimeType'] == "video/mp4":
                    videoUrl = item['videoUrl']
            return videoUrl
        except:
            return ""
        
        