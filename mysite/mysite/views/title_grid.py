"""
author: Connor Oaks
date: 04-17-2023

The purpose of this file is to breakout the title grid logic into it's own place to keep it from being intertwined with the homepage.
This would be very helpful should we ever want to include the title grid anywhere else on the site. 
"""

from mysite import settings
from mysite.models import TitleGridSetting


class TitleGrid: 
    """
    Initialize title grid object. 
    Throws ConnectionError if TMDB API call fails for any reason. 
    """
    def __init__(self, data):
        self.titles = self.create_title_displays(data.json())
        try: 
            pager_setting = TitleGridSetting.objects.get(setting='page selector location')
            self.pager_location = pager_setting.value
        except: 
            self.pager_location = 'bottom'

        if self.pager_location != 'top' and self.pager_location != 'bottom':
            self.pager_location = 'bottom'

    """
    Create title display objects and package them into rows for the template. 
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
