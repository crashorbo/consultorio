$(document).ready(function(){  
  $('#inicio').on('click', function(e){
    e.preventDefault();
    $thisUrl = $(this).attr("href");
    $.ajax({
      method: "get",
      url: $thisUrl,
      success: function(data){
        $("#mainbody").html(data);
      }  
    })
  });

  $('#seguros').on('click', function(e){
    e.preventDefault();
    $thisUrl = $(this).attr("href");
    $.ajax({
      method: "get",
      url: $thisUrl,
      success: function(data){
        $("#mainbody").html(data);
      }  
    })
  });
  $('#servicios').on('click', function(e){
    e.preventDefault();
    $thisUrl = $(this).attr("href");
    $.ajax({
      method: "get",
      url: $thisUrl,
      success: function(data){
        $("#mainbody").html(data);
      }  
    })
  })
  $('#tipolentes').on('click', function(e){
    e.preventDefault();
    $thisUrl = $(this).attr("href");
    $.ajax({
      method: "get",
      url: $thisUrl,
      success: function(data){
        $("#mainbody").html(data);
      }  
    })
  })
  $('#medicamentos').on('click', function(e){
    e.preventDefault();
    $thisUrl = $(this).attr("href");
    $.ajax({
      method: "get",
      url: $thisUrl,
      success: function(data){
        $("#mainbody").html(data);
      }  
    })
  });  
  controlInicio()
});

const controlInicio = () => {
  $.ajax({
    method: "get",
    url: $('#seguros').attr("href"),
    success: function(data){
      $("#mainbody").html(data);
    }  
  });
}

$(function() {
  
  // elementos de la lista
  var menues = $("ul li"); 
  var selector = $("ul li a"); 

  $(menues[0]).addClass("active");
  // manejador de click sobre todos los elementos
  menues.click(function() {
    // eliminamos active de todos los elementos
    menues.removeClass("active");
    selector.removeClass("active");
    // activamos el elemento clicado.
    $(this).addClass("active");
  });

});