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
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', 'https://moviereviewhubcapstone-production-b12e.up.railway.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'whitenoise.runserver_nostatic',
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
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'mysite/templates/',
            'mysite/templates/partial/',
            'mysite/templates/partial/title_grid/'
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
STATIC_URL = '/static/'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', 
    'compressor.finders.CompressorFinder'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Media (Default file save location)
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Compress settings
COMPRESS_ENABLED = True
COMPRESS_ROOT = os.path.join(BASE_DIR, 'staticfiles')
COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'django_libsass.SassCompiler')
]
COMPRESS_OFFLINE = True 
LIBSASS_OUTPUT_STYLE = 'compressed'


# Settings for custom error handling 
ERROR_MESSAGES = {
    1: 'The page could not be found. Please make sure your URL is correct.', 
    2: 'Issue fetching third party content. Please check back again later.',
    3: 'An internal error has occurred, or the page is invalid.',
    4: 'There was an issue executing your requested search. Please try again.'
}
ERROR_RESPONSE_CODES = {
    1: 404, 
    2: 503, 
    3: 500, 
    4: 400
}


# The Movie DB settings
TMDB_API_KEY = 'f670b8f2faa8acefcdb8aa11655d2659'
TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500'
TMDB_GET_MOVIE_URL = 'https://api.themoviedb.org/3/movie/{movieid}?api_key={apikey}&language=en_US'
TMDB_SEARCH_MOVIES_URL = 'https://api.themoviedb.org/3/search/movie?api_key={apikey}&query={query}&include_adult=false'
TMDB_WRITTEN_REVIEWS_URL = 'https://api.themoviedb.org/3/movie/{movieid}/reviews?api_key={apikey}&language=en-US'


# Movie grid settings 
MOVIE_GRID_URLS = {
    'popular-now': 'https://api.themoviedb.org/3/movie/popular?api_key={apikey}&language=en-US&page={page}',
    'now-playing': 'https://api.themoviedb.org/3/movie/now_playing?api_key={apikey}&language=en-US&page={page}', 
    'upcoming': 'https://api.themoviedb.org/3/movie/upcoming?api_key={apikey}&language=en-US&page={page}',
    'recommended': 'https://api.themoviedb.org/3/movie/{movieid}/recommendations?api_key={apikey}&language=en-US&page={page}',
    'search': TMDB_SEARCH_MOVIES_URL
}
HOMEPAGE_MOVIE_GRID_OPTIONS = [
    'popular-now', 
    'now-playing', 
    'upcoming'
]
DEFAULT_HOMEPAGE_DISPLAY = 'popular-now'     # must be one of the homepage movie grid url options. 
DEFAULT_TITLES_PER_ROW = 5 
DEFAULT_PAGER_POSITION = 'top'



# ROTTEN_TOMATO_URL = ''
ROTTEN_TOMATO_GET_MOVIE_URL = 'http://www.omdbapi.com/'
ROTTEN_TOMATO_API_KEY = '18eaeb4f'

#IMDB Offical API
IMDB_API_URL = 'https://imdb-api.com/'
IMDB_API_KEY = 'k_tct5xoj2'

#NYT Movie Review API
NYT_API_URL = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json?query={query}&api-key={apikey}'
NYT_API_KEY = 'KY32UPnw1w22lKgAKZd39Nn7zGECKWHF'
    