$(document).ready(function(){
"use strict"; $(".reaction").on("click",function(){var data_reaction = $(this).attr("data-reaction");
    $(".like-btn-emo").removeClass().addClass('like-btn-emo').addClass('like-btn-'+data_reaction.toLowerCase());
    if(data_reaction === "Like"){$(".like-emo").html('<span class="like-btn-like"></span>');}
    else{$(".like-emo").html('<span class="like-btn-like"></span><span class="like-btn-'+data_reaction.toLowerCase()+'"></span>');}
  });
});
