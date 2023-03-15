/*
      Author: Kevin Flynn
      Date: 02-13-2023

      This file gets the most popluar movies from The Movie Database and creates html
      elements to be displayed on the home page.
*/

"use strict";

var popularMovies = [];
var nowPlayingMovies = [];
var upcomingMovies = [];

const optionsPopular = {
      "async": true,
      "crossDomain": true,
      "url": "https://api.themoviedb.org/3/discover/movie?api_key=f670b8f2faa8acefcdb8aa11655d2659&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_keywords=Jumanji&with_watch_monetization_types=flatrate",
      "method": "GET"
};

const optionsNowPlaying = {
      "async": true,
      "crossDomain": true,
      "url": "https://api.themoviedb.org/3/movie/now_playing?api_key=f670b8f2faa8acefcdb8aa11655d2659&language=en-US&page=1",
      "method": "GET"
};

const optionsUpcoming = {
      "async": true,
      "crossDomain": true,
      "url": "https://api.themoviedb.org/3/movie/upcoming?api_key=f670b8f2faa8acefcdb8aa11655d2659&language=en-US&page=1",
      "method": "GET"
};

$(document).ready(async function(){
      popularMovies = await makeApiCall(optionsPopular);
      createMovieList(popularMovies);
});

async function makeApiCall(options){
      var response = await $.ajax(options);
      console.log(response.results);
      return await response.results;
}

async function switchDisplayedMovies(options, movies){
      if(movies.length === 0)
            movies = await makeApiCall(options);

      createMovieList(movies);

      return movies;
}

function createMovieList(movies){
      $("#movieList").empty();
      let element = $("#movieList");
      for(let i = 0; i < movies.length; i++){
            if(i % 5 == 0){
                  element = $("<tr>");
                  $("#movieList").append(element);
            }
            createMovieCard(movies[i], element);
      }
}

function createMovieCard(movie, element){
      const $poster = $("<td>").addClass("movieList-item").data("title", movie.title).attr("onclick", "viewDetailsPage("+movie.id+")");

      // Create the image element and set the src and alt attributes
      const $image = $("<img>").attr("src", "https://image.tmdb.org/t/p/w500"+movie.poster_path).attr("alt", movie.title);

      // Create the title element and set the text content
      const $title = $("<p>").text(movie.title);

      //Create arrow icon
      const $arrow = $("<span>").addClass("material-symbols-outlined").text("arrow_circle_right");

      // Append the image and title elements to the poster div
      $poster.append($image, $title, $arrow);

      // Append the poster div to the grid container
      $(element).append($poster);
}

function viewDetailsPage(movieId) {
      window.location += `titles/${movieId}`
}

$("#popular-now").click(async function(){ popularMovies = await switchDisplayedMovies(optionsPopular, popularMovies)});

$("#now-playing").click(async function(){ nowPlayingMovies = await switchDisplayedMovies(optionsNowPlaying, nowPlayingMovies) });

$("#upcoming").click(async function(){ upcomingMovies = await switchDisplayedMovies(optionsUpcoming, upcomingMovies) });