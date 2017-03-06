$(document).ready(initSetup);

function initSetup(){
  var initHeight = $(window).height();
  ajustesIniciales();

  function ajustesIniciales(){
    $("section#bodyList").css({
        var height = 10;
      "height": height +"px;"
    });

    $("section#mainPhoto").css({
      "height": initHeight +"px;"
    });
  }

  $(document).scroll(scrollFunction);

  function scrollFunction(){
    var scrollTop = $(this).scrollTop();
    var pixels = scrollTop / 70;

  }
}
