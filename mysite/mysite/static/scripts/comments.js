/**
 * Author: Kevin Flynn
 * Date: 04-12-2023
 * 
 * This file contains the client side scripting for comments (used in tmdb_comments.html) 
 */

$(document).ready(function(){
      $(".show-txt-btn").click(function(){
         $(this).prev().toggle();
         $(this).siblings('.dots').toggle();
         if($(this).text()=='read more'){
         $(this).text('read less');
         }
         else{
         $(this).text('read more');
         }
      });
   });