

"use strict";

const options = {
      "async": true,
      "crossDomain": true,
      "url": "https://api.themoviedb.org/3/discover/movie?api_key=f670b8f2faa8acefcdb8aa11655d2659&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_keywords=Jumanji&with_watch_monetization_types=flatrate",
      "method": "GET"
};

$.ajax(options).done(function (response) {
      console.log(response);

      for(let i = 0; i < response.results.length; i++){
            createMovieCard(response.results[i]);
      }
});

function createMovieCard(movie){
      var movieCard = document.createElement("div");

      var poster = document.createElement("img");
      poster.setAttribute("src", "https://api.themoviedb.org/3/discover/movie?api_key=f670b8f2faa8acefcdb8aa11655d2659" + movie.poster_path)
      movieCard.appendChild(poster);

      var title = document.createTextNode(movie.title);
      movieCard.appendChild(title);
      document.body.appendChild(movieCard);
}

