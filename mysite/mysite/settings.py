"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5*&*4cvn3^-j7von=ff*1op&7er=q#h!72hgtdacpur#fk%w6n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'moviereviewhub.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite',
    'compressor'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'mysite/templates/',
            'mysite/templates/partial/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'mysite/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mysite', 'static'),
    os.path.join(BASE_DIR, 'mysite', 'static', 'scripts'),
    os.path.join(BASE_DIR, 'mysite', 'static', 'styles'),
    os.path.join(BASE_DIR, 'mysite', 'static', 'images')
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', 
    'compressor.finders.CompressorFinder'
]

# Media (Default file save location)
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Compress settings
COMPRESS_ROOT = os.path.join(BASE_DIR, 'mysite', 'static', 'styles')
COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'django_libsass.SassCompiler')
]


# Settings for custom error handling 
ERROR_MESSAGES = {
    '1': 'The page could not be found. Please make sure your URL is correct.', 
    '2': 'Issue fetching third party content. Please check back again later.',
    '3': 'An internal error has occurred, or the page is invalid.',
    '4': 'There was an issue executing your requested search. Please try again.'
}
ERROR_RESPONSE_CODES = {
    '1': 404, 
    '2': 503, 
    '3': 500, 
    '4': 400
}


# The Movie DB settings
TMDB_API_KEY = 'f670b8f2faa8acefcdb8aa11655d2659'
TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500'
TMDB_GET_MOVIE_URL = 'https://api.themoviedb.org/3/movie/{movieid}?api_key={apikey}&language=en_US'
TMDB_SEARCH_MOVIES_URL = 'https://api.themoviedb.org/3/search/movie?api_key={apikey}&query={query}&include_adult=true'
TMDB_MOVIE_GRID_URLS = {
    'popular-now': 'https://api.themoviedb.org/3/movie/popular?api_key={apikey}&language=en-US&page=1', 
    'now-playing': 'https://api.themoviedb.org/3/movie/now_playing?api_key={apikey}&language=en-US&page=1', 
    'upcoming': 'https://api.themoviedb.org/3/movie/upcoming?api_key={apikey}&language=en-US&page=1',
}
DEFAULT_HOMEPAGE_DISPLAY = 'popular-now'     # must be one of the movie grid url options. 


# IMDb settings
IMDB_DATASET_ROOT = os.path.join(MEDIA_ROOT, 'datasets')
IMDB_DATASET_URL = 'https://datasets.imdbws.com/title.ratings.tsv.gz'
IMDB_DATASET = {
    'filename': 'imdb_ratings.tsv', 
    'tsv_fields': ['tconst', 'averageRating', 'numVotes'],
    'db_fields': ['unique_id', 'rating', 'votes']
}

# ROTTEN_TOMATO_URL = ''
ROTTEN_TOMATO_GET_MOVIE_URL = 'http://www.omdbapi.com/'
ROTTEN_TOMATO_API_KEY = '18eaeb4f'

# IMBD_GET_MOVIE_URL = ''
# IMBD_GET_MOVIE_URL = ''
# IMDB_API_KEY = ''

    