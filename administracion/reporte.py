import os

from datetime import datetime
from io import BytesIO

from django.http import HttpResponse
from django.conf import settings

from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, portrait
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib import colors

def encabezado(canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 8)        
        archivo_imagen1 = os.path.join(settings.MEDIA_ROOT, "imagenes","sistema","logo1.jpg")
        archivo_imagen2 = os.path.join(settings.MEDIA_ROOT, "imagenes","sistema","logo2.jpg")         
        canvas.drawImage(archivo_imagen1, 1.5*cm, 720,width=60, height=40)
        canvas.drawImage(archivo_imagen2, 8.1*cm, 720,width=150, height=40)        
        canvas.restoreState()

def pie(canvas, doc):
    hoy = datetime.now()        
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(19*cm, cm, 'Pagina {}'.format(doc.page))
    canvas.drawString(1.5*cm, cm, 'Fecha de impresión: {}'.format(hoy.strftime('%d/%m/%Y - %H:%M')) )
    canvas.restoreState()

def reporte_particular(registro, registros, total):
    hoy = datetime.now()    
    response = HttpResponse(content_type='application/pdf')
    # se crea el nombre del archivo de la descarga pdf
    pdf_name = 'particulares_{}.pdf'.format(hoy.strftime("%Y%m%d"))
    response['Content-Disposition'] = 'inline; filename={}'.format(pdf_name)
    # se crea el buffer de memoria para generar el documento
    buffer = BytesIO()
    # configuracion de documento base para la plantilla
    doc = BaseDocTemplate(buffer,
                          pagesize=letter, 
                          leftMargin=1.5*cm,
                          rightMargin=1.5*cm,
                          topMargin=1.5*cm,
                          bottomMargin=1.5*cm
                          )
    frame0 = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - cm, showBoundary=0, id='bordeNormal')
    doc.addPageTemplates([PageTemplate(id='principal', frames=frame0, onPage=encabezado, onPageEnd=pie),])

    #Creamos la hoja de Estilo
    estilo=getSampleStyleSheet()
    estilo.add(ParagraphStyle(name='centered', alignment=TA_CENTER, fontSize=12, leading=20))
    #Iniciamos el platypus story
    story = []

    asegurados = []

    story.append(Paragraph('<b>CONSULTAS PARTICULARES</b>', estilo['centered']))
    story.append(Paragraph('del <i>{}</i> al <i>{}</i>'.format(registro.fecha_inicio.strftime("%d/%m/%Y"),registro.fecha_fin.strftime("%d/%m/%Y")), estilo['centered']))
    cabecera = ParagraphStyle(name="cabecera", alignment=TA_CENTER, fontSize=10, fontName="Times-Roman", textColor=colors.white)
    celda = ParagraphStyle(name="celda", alignment=TA_LEFT, fontsize=8, fontName="Times-Roman")    
    celdaDerecha = ParagraphStyle(name="celdaDerecha", alignment=TA_RIGHT, fontsize=8, fontName="Times-Roman")
    it = 1
    for ingreso in registros:
        if not ingreso.costo == 0:  
            asegurado = [Paragraph('{}'.format(it), celda), Paragraph(ingreso.fecha.strftime("%d/%m/%Y"), celda), Paragraph('{} {}'.format(ingreso.agenda.paciente.nombres, ingreso.agenda.paciente.apellidos), celda), 
            Paragraph(ingreso.servicio.nombre,celda), Paragraph('{}'.format(ingreso.costo), celdaDerecha)]
            asegurados.append(asegurado)
            it = it+1
    total = [Paragraph('<b>TOTAL</b>', celda), '','','',Paragraph('<b>{0:.2f}</b>'.format(total or '0.00'), celdaDerecha)]    
    asegurados.append(total)
    headings = (Paragraph('Nº', cabecera), Paragraph('FECHA', cabecera), Paragraph('NOMBRE DEL PACIENTE', cabecera), Paragraph('SERVICIO', cabecera), Paragraph('MONTO', cabecera))
    tabla = Table([headings] + asegurados, colWidths=[1*cm, 2.5*cm, 7.5*cm, 3.5*cm, 2*cm], style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),0.5,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.black),
                       ('SPAN', (-2,-1), (0,-1))
                       ]
              )
    story.append(tabla)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def reporte_seguro(registro, registros, total):
    hoy = datetime.now()    
    response = HttpResponse(content_type='application/pdf')
    # se crea el nombre del archivo de la descarga pdf
    pdf_name = 'seguros_{}.pdf'.format(hoy.strftime("%Y%m%d"))
    response['Content-Disposition'] = 'inline; filename={}'.format(pdf_name)
    # se crea el buffer de memoria para generar el documento
    buffer = BytesIO()
    # configuracion de documento base para la plantilla
    doc = BaseDocTemplate(buffer,
                          pagesize=letter, 
                          leftMargin=1.5*cm,
                          rightMargin=1.5*cm,
                          topMargin=1.5*cm,
                          bottomMargin=1.5*cm
                          )
    frame0 = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - cm, showBoundary=0, id='bordeNormal')
    doc.addPageTemplates([PageTemplate(id='principal', frames=frame0, onPage=encabezado, onPageEnd=pie),])

    #Creamos la hoja de Estilo
    estilo=getSampleStyleSheet()
    estilo.add(ParagraphStyle(name='centered', alignment=TA_CENTER, fontSize=12, leading=20))
    #Iniciamos el platypus story
    story = []

    asegurados = []

    story.append(Paragraph('<b>{}</b>'.format(registro.seguro.nombre), estilo['centered']))
    story.append(Paragraph('del <i>{}</i> al <i>{}</i>'.format(registro.fecha_inicio.strftime("%d/%m/%Y"),registro.fecha_fin.strftime("%d/%m/%Y")), estilo['centered']))
    cabecera = ParagraphStyle(name="cabecera", alignment=TA_CENTER, fontSize=10, fontName="Times-Roman", textColor=colors.white)
    celda = ParagraphStyle(name="celda", alignment=TA_LEFT, fontsize=8, fontName="Times-Roman")    
    celdaDerecha = ParagraphStyle(name="celdaDerecha", alignment=TA_RIGHT, fontsize=8, fontName="Times-Roman")
    it = 1
    for ingreso in registros:
        if not ingreso.costo == 0:  
            asegurado = [Paragraph('{}'.format(it), celda), Paragraph(ingreso.fecha.strftime("%d/%m/%Y"), celda), Paragraph('{} {}'.format(ingreso.agenda.paciente.nombres, ingreso.agenda.paciente.apellidos), celda), 
            Paragraph('{}'.format(ingreso.agenda.matricula), celda), Paragraph(ingreso.agenda.tipo_beneficiario, celda), Paragraph(ingreso.servicio.nombre[2:],celda),
            Paragraph('{}'.format(ingreso.costo), celdaDerecha)]
            asegurados.append(asegurado)
            it = it+1
    total = [Paragraph('<b>TOTAL</b>', celda), '','','','','',Paragraph('<b>{0:.2f}</b>'.format(total or '0.00'), celdaDerecha)]    
    asegurados.append(total)
    headings = (Paragraph('Nº', cabecera), Paragraph('FECHA', cabecera), Paragraph('NOMBRE DEL PACIENTE', cabecera), Paragraph('MATRIC.', cabecera), Paragraph('TIPO', cabecera), Paragraph('SERVICIO', cabecera), Paragraph('MONTO', cabecera))
    tabla = Table([headings] + asegurados, colWidths=[1*cm, 2.1*cm, 6.5*cm, 2.8*cm, 1.5*cm, 3*cm, 2*cm], style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),0.5,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.black),
                       ('SPAN', (-2,-1), (0,-1))
                       ]
              )
    story.append(tabla)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response