# Movie Review Hub Capstone
Welcome to the GitHub for the University of Wisconsin-Milwaukee's 2023 Computer Science Capstone Project - Group 4. Movie Review Hub is a one stop shop for movie lovers to get a clear picture of how a film has been recieved across the board based on both ratings and written reviews on many different online platforms.

# Data Sources
We use many different existing APIs to pull in data about the films featured on our site:

## [The Movie Database](https://developers.themoviedb.org/3/getting-started/introduction)
We use a few different API endpoints hosted by The Movie Database in the implementation of our "Movie Grid" widget as seen on our home page and at the bottom of each movie page for recommendations. It's also how we power our search functionality on the homepage, and since they have their own review system they're one of our sources for ratings and reviews.

## Ratings & Reviews
Here are the sources of the ratings we feature on movie pages, these also factor into the overall/average score:
- [IMDb](https://www.imdb.com/)
- [Rotten Tomatoes](https://www.rottentomatoes.com/)
- [Metacritic](https://www.metacritic.com/)
- [The Movie DB](https://www.themoviedb.org/)

For written reviews: 
- Once again, [The Movie DB](https://www.themoviedb.org/)
- [The New York Times](https://www.nytimes.com/reviews/movies)

# Local Configurations
The following are the steps to set up a local instance of the Movie Review Hub site for development purposes. 

## Clone The Repository
You can use either HTTPS or SSH for cloning, though you must first be added to the repository by one of the owners. Here are the Git Bash commands to clone the repositiory using HTTPS and SSH respectively:

`git clone https://github.com/kflynn45/MovieReviewHubCapstone.git`

`git clone git@github.com:kflynn45/MovieReviewHubCapstone.git`

## Install Required Packages
We use a number of third party packages for different bits of critical functionality. For instance, all of the API calls made on the backend use the `requests` module, and we use `compress` and `whitenoise` to enable SCSS and to allow for serving static files with a production configuration. To install all neccesary modules based on our current `requirements.txt`, navigate to the root folder and run the following:

```
pip install -r requirements.txt
```

## Setup Local SQLite Database
Our site isn't data intesive, and we are using the default SQLite database configuration that comes packaged with Django. To create the local database and the proper tables based on `models.py`, navigate to the folder containing `manage.py` and run the following commands:

```
python manage.py makemigrations
python manage.py migrate
```
**Note:** Depending on your python configuration, you may need to use "python3 ..." for management commands. 

## Create Static Files
For simplicity sake, we try to keep our local configurations as close to the production environment as possible. Because of this we recommend treating static files as such and running the local web server with `whitenoise` as opposed to Django's packaged static files server for development environments. 

Before running the local web server or before your final push before opening a pull request, run the following commands: 

```
python manage.py collectstatic --noinput
python manage.py compress
```

## Test Your Local Movie Review Hub
At this point you should have a functioning development & testing environment! Run the local web server with the following command: 

```
python manage.py runserver
```

You should now be able to see Movie Review Hub in your browser when you navigate to whichever port you've configured the local web server to run on. Default is http://127.0.0.1:8000

Some specific bits of functionality to test:
- Click between each of the tabs above the movie grid on the homepage.
- Use the page selector to switch pages, try entering a random number/value.
- Search using the search bar and make sure you get relevant results.
- Try viewing a few different individual movie pages and make sure everything looks correct.
- Try watching a trailer on one of the movie pages. 
- Try to visit a page that doesn't exist within the Movie Review Hub site. You should be directed to the error page. 
- Refresh each page with the "Network" tab in your browser's developer console open to check for any errors with serving files or making HTTP requests on the site. 

## Optional Admin Settings
To make certain elements on the site somewhat customizable without needing to push code changes, we created a data model for settings to be configurable in the admin panel. To get access to the admin panel for your local site, you will need to create a super user by running the following command: 

```
python manage.py createsuperuser
```
Follow the prompts to enter the username and password for your new user. After this is complete you can login to the admin panel by navigating to `*your local site url*/admin`. From the admin panel you will be able to see the data models that correspond to different types of settings. Here are the settings currently in use, which you can add as you wish to customize aspects of your local site: 

### Title Grid Settings
- Page Selector Location 
    - Setting: "page selector location"
    - Value: Either "bottom" or "top"
- Titles Per Row
    - Setting: "titles per row"
    - Value: Positive integer

**Note:** Configuring any of these settings isn't necessary for the site to work. Default values for each can be found in `settings.py`






