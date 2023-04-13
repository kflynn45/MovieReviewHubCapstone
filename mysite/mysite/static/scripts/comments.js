// function dynamicSizeComment() {
//       var dots = document.getElementById("dots");
//       var readMoreText = document.getElementById("show-txt-area");
//       var btnText = document.getElementById("show-txt-btn");
    
//       if (dots.style.display === "none") {
//         dots.style.display = "inline";
//         btnText.innerHTML = "Read more"; 
//         readMoreText.style.display = "none";
//       } else {
//         dots.style.display = "none";
//         btnText.innerHTML = "Read less"; 
//         readMoreText.style.display = "inline";
//       }
//     }

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