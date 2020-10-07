const pickerInicio = document.getElementById("datepicker-inicio");
const pickerFin = document.getElementById("datepicker-fin");
const fechaPickerInicio = document.getElementById("fecha-datepicker-inicio");
const fechaPickerFin = document.getElementById("fecha-datepicker-fin")

moment.locale("es");

// Inicializacion del datepicker
const datepickerInicio = new Datepicker(pickerInicio, {
    buttonClass: 'btn',
    language: 'es',
    autohide: true,
    format:'yyyy-mm-dd',
 });
 const datepickerFin = new Datepicker(pickerFin, {
    buttonClass: 'btn',
    language: 'es',
    autohide: true,
    format:'yyyy-mm-dd',
 })
datepickerInicio.setDate(new Date());
datepickerFin.setDate(new Date());
fechaPickerInicio.innerHTML = moment(pickerInicio.value).format('dddd - MMMM DD, YYYY');
fechaPickerFin.innerHTML = moment(pickerFin.value).format('dddd - MMMM DD, YYYY');