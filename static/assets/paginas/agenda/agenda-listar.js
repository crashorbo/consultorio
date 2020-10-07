const loader = `<div id="loading"></div>`;
const elem = document.getElementById("datepicker");
const fechaDatepicker = document.getElementById("fecha-datepicker");
const navIzq = document.getElementById("navizq");
const navDer = document.getElementById("navder");
const listaConsulta = document.getElementById("lista-consultas");
const searchForm = document.getElementById("search-form");
const imprimir = document.getElementById("imprimir");

moment.locale('es');
// Inicializacion del datepicker
const datepicker = new Datepicker(elem, {
  buttonClass: 'btn',
  language: 'es',
  autohide: true,
  format:'yyyy-mm-dd',
})
datepicker.setDate(new Date());
fechaDatepicker.innerHTML = moment(elem.value).format('dddd - MMMM DD, YYYY');
// funcion que devuelve lista de pacientes
const getPacientes = () => {
  listaConsulta.innerHTML = loader;
  fetch(searchForm.getAttribute("action"), {
    method: 'post',
    body: new FormData(searchForm)
  })
  .then(response => response.text())
  .then(text => listaConsulta.innerHTML = text);  
}
getPacientes();
// evento cuando se cambia la fecha fecha
elem.addEventListener('changeDate', e => {
  fechaDatepicker.innerHTML = moment(elem.value).format('dddd - MMMM DD, YYYY');    
  getPacientes();
});

navIzq.addEventListener("click", e => {
  let fecha = moment(datepicker.getDate()).subtract(1, 'd').format('YYYY-MM-DD');
  datepicker.setDate(fecha);
})

navDer.addEventListener("click", e => {
  let fecha = moment(datepicker.getDate()).add(1, 'd').format('YYYY-MM-DD');
  datepicker.setDate(fecha);
})

// evento de click en una fila
listaConsulta.addEventListener("click", e => {
  e.preventDefault();
  const auxTarget = e.target.closest(".schedule-item");
  if (auxTarget) {
    window.location.href = auxTarget.getAttribute("data-url");
  }  
})

// imprimir reporte por fecha
imprimir.addEventListener('click', e => {
  fecha = moment(elem.value).format('DD-MM-YYYY');
  this_url = '/agenda/movimiento/reportemovfecha/'+fecha;
  window.open(this_url,"reporte","height=600,width=700,status=no, toolbar=no,menubar=no,location=no,scrollbars=yes");
})