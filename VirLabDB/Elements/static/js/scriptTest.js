$(document).ready(initFunction);
  function initFunction(){
  var height = $(window).height();
  ajustesIniciales();

  function ajustesIniciales(){
    $("section#body").css({
      "margin-top": height - 80 + "px"
    });
  }

  $(document).scroll(scrollFunction);

  function scrollFunction(){
      var scrollTop = $(this).scrollTop();
      var pixels = scrollTop / 70;

      if(scrollTop < height){
        $("section#contenedorGeneral").css({
            "-webkit-filter": "blur(" + pixels + "px)",
            "background-position": "center -" + pixels * 10 + "px"
        });
      }
  }
}
