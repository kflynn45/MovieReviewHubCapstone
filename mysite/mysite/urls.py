"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import settings
from mysite.views.home import Home
from mysite.views.title_details import TitleDetails
from mysite.views.title_grid import refresh_titles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), {'action': settings.DEFAULT_HOMEPAGE_DISPLAY}, name='index'),
    path('<action>', Home.as_view(), name='tab_view'), 
    path('title_grid/refresh', refresh_titles, name='grid_refresh'),
    path('titles/<title_id>', TitleDetails.as_view())
]

# Overrides for 404/500 pages (does not apply when in debug mode)
handler404 = 'mysite.views.error.handle_404'
handler500 = 'mysite.views.error.handle_500'