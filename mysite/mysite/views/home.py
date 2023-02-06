"""
Author: Connor Oaks
Date: 02-01-2023

This file contains the server side portion of the homepage.  
"""

from django.views import View
from django.shortcuts import render


class Home(View):
    """
    Process GET requests for the homepage. 
    """
    def get(self, request):
        return render(request, "home.html", {})