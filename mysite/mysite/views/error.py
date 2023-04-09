"""
Author: Connor Oaks
Date: 04-06-2023

This file contains the error page view as well as overrides for the default 404 & 500 error pages.
"""

from django.shortcuts import render
from mysite import settings


"""
Render the custom error page and return the apropriate response code to the client.
"""
def render_error(request, error_number):
    response = render(request, 'error.html', {
        'message': settings.ERROR_MESSAGES[error_number] 
    })
    response.status_code = settings.ERROR_RESPONSE_CODES[error_number]
    return response

def handle_404(request, *args, **kwargs):
    return render_error(request, 1)

def handle_500(request): 
    return render_error(request, 3)
