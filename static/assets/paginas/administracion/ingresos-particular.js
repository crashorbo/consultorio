const generarReporte = document.getElementById("generar-reporte");
const ventanaModal = document.getElementById("responsive-modal");
const contenidoModal = document.getElementById("contenido-modal");
const waypointContainer = document.getElementById("tabla-particulares");
const ingFechaInicio = document.getElementById("ingreso-fecha-inicio");
const ingFechaFin = document.getElementById("ingreso-fecha-fin");
const loader = `<div id="loading"></div>`;

datepickerIngFechaInicio = new Datepicker(ingFechaInicio, {
    buttonClass: 'btn',
    language: 'es',
    autohide: true,
    format: 'dd/mm/yyyy',    
});

datepickerIngFechaFin = new Datepicker(ingFechaFin, {
    buttonClass: 'btn',
    language: 'es',
    autohide: true,
    format: 'dd/mm/yyyy',
});

datepickerIngFechaInicio.setDate(new Date());
datepickerIngFechaFin.setDate(new Date());


const waypoint = new Waypoint.Infinite({
    element: waypointContainer,
    offset: 'bottom-in-view'
})

generarReporte.addEventListener("click", e => {
    e.preventDefault();
    fetch(e.target.getAttribute("data-url"))
    .then(res => res.text())
    .then(text => {        
        contenidoModal.innerHTML = text;
        const pickerInicio = document.getElementById('id_fecha_inicio');
        const pickerFin = document.getElementById('id_fecha_fin')
        datepickerInicio = new Datepicker(pickerInicio, {
            buttonClass: 'btn',
            language: 'es',
            autohide: true,
            format: 'dd/mm/yyyy',
            container: '#responsive-modal'
        });
        datepickerFin = new Datepicker(pickerFin, {
            buttonClass: 'btn',
            language: 'es',
            autohide: true,
            format: 'dd/mm/yyyy',
            container: '#responsive-modal'
        });
        datepickerInicio.setDate(new Date());
        datepickerFin.setDate(new Date());
        $("#responsive-modal").modal('show')
        const formIngresos = document.getElementById("form-ingresos")
        formIngresos.addEventListener("submit", e => {
            e.preventDefault();
            const urlForm = e.target.getAttribute('action');
            const data = new FormData(e.target);
            fetch(urlForm, {
                method: "post",
                body: data
            })
            .then(res => res.text())            
            .then(text => window.location.reload())
        })
    });
});

waypointContainer.addEventListener("click", e => {    
    if (e.target.parentNode.tagName.toLowerCase() === 'a' && !(e.target.parentNode.getAttribute("target") === '_blank')){
        e.preventDefault();
        const url = e.target.parentNode.getAttribute("href");
        fetch(url)
        .then(res => res.text())
        .then(text => {
            contenidoModal.innerHTML = text;
            const pickerDeposito = document.getElementById('id_fecha_deposito');
            datepickerDeposito = new Datepicker(pickerDeposito, {
                buttonClass: 'btn',
                language: 'es',
                autohide: true,
                format: 'dd/mm/yyyy',
                container: '#responsive-modal'
            });
            datepickerDeposito.setDate(new Date());
            const photo = document.getElementById("id_photo");
            photo.addEventListener('change', e =>{                
                if(e.target.files.length > 0){                    
                    const src = URL.createObjectURL(e.target.files[0]);                    
                    const preview = document.getElementById("deposito-photo");                    
                    preview.src = src;
                }
            })
            $("#responsive-modal").modal('show');
            const formDeposito = document.getElementById("form-deposito")
            formDeposito.addEventListener("submit", e => {
                e.preventDefault();
                const urlForm = e.target.getAttribute('action');
                const data = new FormData(e.target);
                fetch(urlForm, {
                    method: "post",
                    body: data
                })
                .then(res => res.text())
                .then(text => window.location.reload())      
            })
        })
    }        
});

const filtroFechas = () => {    
    let fechaValues = {
        'fechaini': moment(datepickerIngFechaInicio.getDate()).format('YYYY-MM-DD'),
        'fechafin': moment(datepickerIngFechaFin.getDate()).format('YYYY-MM-DD')
    }
    fetch('/administracion/ingresos-particular-filtro/?' + new URLSearchParams(fechaValues))
    .then(res => res.text())
    .then(text => {
        waypointContainer.innerHTML = text;
        document.getElementById("display-total").innerHTML = document.getElementById("suma-total").value;
    })    
}

ingFechaInicio.addEventListener('changeDate', () => {
    filtroFechas();
})

ingFechaFin.addEventListener('changeDate', () => {
    filtroFechas();
})