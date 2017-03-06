$(document).ready(initSetup);

function initSetup(){
  var initHeight = $(window).height();
  ajustesIniciales();

  function ajustesIniciales(){}
  $("section#mainPhoto").css({
    "height": initHeight +"px;"
  });


  $(document).scroll(scrollFunction);

  function scrollFunction(){
    var scrollTop = $(this).scrollTop();
    var pixels = scrollTop / 70;

    }
  }
}
