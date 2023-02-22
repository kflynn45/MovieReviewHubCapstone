/*
      Author: Kevin Flynn
      Date: 02-13-2023

      This file gets the most popluar movies from The Movie Database and creates html
      elements to be displayed on the home page.
*/

"use strict";

$(document).ready(function(){

      const options = {
            "async": true,
            "crossDomain": true,
            "url": "https://api.themoviedb.org/3/discover/movie?api_key=f670b8f2faa8acefcdb8aa11655d2659&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_keywords=Jumanji&with_watch_monetization_types=flatrate",
            "method": "GET"
      };
      
      $.ajax(options).done(function (response) {
            console.log(response);
      
            let element = $("#movieList");
            for(let i = 0; i < response.results.length; i++){
                  if(i % 5 == 0){
                        element = $("<tr>");
                        $("#movieList").append(element);
                  }
                  createMovieCard(response.results[i], element);

            }
      });
    
    });

function createMovieCard(movie, element){
      const $poster = $("<td>").addClass("movieList-item").data("title", movie.title);

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