$(document).ready(initSetup);

function initSetup(){
  var initHeight = $(window).height();
  ajustesIniciales();

  function ajustesIniciales(){


    $("section#mainPhoto").css({
      "height": initHeight +"px;"
    });
  }

  var flag = false;
  var scroll;

  $(window).scroll(scrollFunction_);

  function scrollFunction_(){
    scroll = $(window).scrollTop();

    if(scroll > 200){
      if(!flag){
        $("#title").css({
          "margin-top": "-23px",
          "width": "400px",
          "height": "75px",
        });
        $("#scrollText").css({
          "color": "transparent";
        });
        flag = true;
      }
    }else{
      if(flag){
        $("#title").css({
          "margin-top": "300px",
          "width": "450px",
          "height": "100px",
        });
        $(""#scrollText").css({
          "color": "white";
        });

        flag = false;
      }
    }
  }
}
