$(document).ready(function(){

  var calendar = $('#calendar').fullCalendar({
    defaultView: 'agendaDay',
    slotDuration: '00:15',
    minTime: '08:00:00',
    maxTime: '22:00:00',
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },
    eventLimit: true,
    events: 'ajax-lista',
    eventClick: function (event) {
      $.ajax({
        url: 'editarajax/'+event.id,
        type: 'get',  
        success: function(data){
            $('#contenido-modal').html(data);
            $('#responsive-modal').modal('show');
        }
      })
    }
  });

  recalculo();

  $('#id_paciente').select2({
    language: 'es',
    ajax: {
      url: "paciente-autocomplete/",
      dataType: 'json',
      delay: 250,
      data: function(params) {
          return {
              q: params.term, // search term
              page: params.page
          };
      },
      processResults: function(data, params) {
          // parse the results into the format expected by Select2
          // since we are using custom formatting functions we do not need to
          // alter the remote JSON data, except to indicate that infinite
          // scrolling can be used
          params.page = params.page || 1;
          return {
              results: data.results,
              pagination: {
                  more: (params.page * 30) < data.total_count
              }
          };
      },
    cache: true
    },
    escapeMarkup: function(markup) {
        return markup;
    }, // let our custom formatter work
    minimumInputLength: 2,
    
  });
 
  $('.clockpicker').clockpicker({
    donetext: 'Done',
  }).find('input').change(function() {
    console.log(this.value);
  });
  $('#id_fecha').datepicker({
    autoclose: true,
    todayHighlight: true,
    format: "dd/mm/yyyy",
    language: 'es',
  });
  $('#form-agenda').on('submit', function (e) {
    e.preventDefault();
    var $formData = $(this).serialize();
    var $formArray = $(this).serializeArray();
    var $formArray = {};
    $.each($(this).serializeArray(), function (i, field) {
      $formArray[field.name] = field.value; 
    });
    var $thisUrl = $(this).attr('action');
    var $thisMethod = $(this).attr('method');
    $.ajax({
        method: $thisMethod,
        url: $thisUrl,
        data: $formData,
        success: function(data){
          $("#msj-modal").html(data);
          $("#responsive-modal").modal('hide');
          $('#calendar').fullCalendar("refetchEvents");
          $('#form-agenda')[0].reset();
          $("#id_paciente").val("").trigger("change");
          $(".seguro-seleccion").hide();
          $("#mensaje-modal").modal('show');
          window.recalculo();
          costo();
        },
        error: function(xhr,errmsg,err) {
          // Show an error
          $('#results').html("<div class='alert-box alert radius' data-alert>"+
          "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    })
  });

  $("#registro-paciente").click(function(){
    var getUrl = window.location;
    $.ajax({
      url: getUrl.protocol + "//" + getUrl.host+'/paciente/registrar',
      type: 'get',  
      success: function(data){
          $('#contenido-modal').html(data);
      }
    })
  });
  document.addEventListener('keypress', function(evt) {

    // Si el evento NO es una tecla Enter
    if (evt.key !== 'Enter') {
      return;
    }
    
    let element = evt.target;
  
    // Si el evento NO fue lanzado por un elemento con class "focusNext"
    if (!element.classList.contains('focusNext')) {
      return;
    }
  
    // AQUI logica para encontrar el siguiente
    let tabIndex = element.tabIndex + 1;
    var next = document.querySelector('[tabindex="'+tabIndex+'"]');
  
    // Si encontramos un elemento
    if (next) {
      next.focus();
      event.preventDefault();
    }
  });
  $(".seguro-seleccion").hide();
  $('#id_tipo').change(function(e){
    if($(this).val() == 0)
      $(".seguro-seleccion").hide();
    else
      $(".seguro-seleccion").show();
  });
  costo();
});

$("#id_agendaserv-0-servicio").on("change", function(){
  costo();
});

function costo(){
  var servicioId = $("#id_agendaserv-0-servicio").val();
  $.ajax({
    url: "/servicio-costo",
    data: {"id": servicioId},
    type: "get",
    success: function(data){
      $("#id_agendaserv-0-costo").val(data.costo);
    }
  });

}

window.recalculo = function (){
  var getUrl = window.location;
  $.ajax({
    url: getUrl.protocol + "//" + getUrl.host+'/movcalculo', 
    type: 'get',  
    success: function(data){        
        window.document.getElementById('sis_ingresos').value = data.ingreso + ' Bs.';
        $("#sis_ingresos").text(data.ingreso + ' Bs.');
        $("#sis_egresos").text(data.egreso + ' Bs.');
        $("#sis_total").text((Number(data.ingreso) - Number(data.egreso)).toFixed(2) + ' Bs.');
    }
  })
};

function imprimirlista(e, obj)
{
  e.preventDefault();
  this_url = $(obj).attr('href');
  window.open(this_url,"reporte","height=700,width=700,status=no, toolbar=no,menubar=no,location=no,scrollbars=yes");
}
