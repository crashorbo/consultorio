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
        canvas.drawImage(archivo_imagen1, 2.5*cm, 720,width=60, height=40)
        canvas.drawImage(archivo_imagen2, 8.6*cm, 720,width=150, height=40)        
        canvas.restoreState()

def pie(canvas, doc):
    hoy = datetime.now()        
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(19*cm, cm, 'Pagina {}'.format(doc.page))
    canvas.drawString(2.5*cm, cm, 'Fecha de impresión: {}'.format(hoy.strftime('%d/%m/%Y - %H:%M')) )
    canvas.restoreState()

def reporte_seguro(registro, registros, total):
    hoy = datetime.now()    
    response = HttpResponse(content_type='application/pdf')
    # se crea el nombre del archivo de la descarga pdf
    pdf_name = 'seg_{}.pdf'.format(hoy.strftime("%Y%m%d"))
    response['Content-Disposition'] = 'inline; filename={}'.format(pdf_name)
    # se crea el buffer de memoria para generar el documento
    buffer = BytesIO()
    # configuracion de documento base para la plantilla
    doc = BaseDocTemplate(buffer,
                          pagesize=letter, 
                          leftMargin=2.5*cm,
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
            asegurado = [Paragraph('{}'.format(it), celda), Paragraph('{} {}'.format(ingreso.agenda.paciente.nombres, ingreso.agenda.paciente.apellidos), celda), 
            Paragraph('{}'.format(ingreso.agenda.matricula), celda), Paragraph(ingreso.agenda.tipo_beneficiario, celda), Paragraph(ingreso.servicio.nombre,celda),
            Paragraph(ingreso.fecha.strftime("%d/%m/%Y"), celda), Paragraph('{}'.format(ingreso.costo), celdaDerecha)]
            asegurados.append(asegurado)
            it = it+1
    total = [Paragraph('<b>TOTAL</b>', celda), '','','','','',Paragraph('<b>{}</b>'.format(total or '0.00'), celdaDerecha)]    
    asegurados.append(total)
    headings = (Paragraph('Nº', cabecera), Paragraph('NOMBRE DEL PACIENTE', cabecera), Paragraph('MATRIC.', cabecera), Paragraph('TIPO', cabecera), Paragraph('SERVICIO', cabecera), Paragraph('FECHA', cabecera), Paragraph('MONTO', cabecera))
    tabla = Table([headings] + asegurados, colWidths=[0.8*cm, 6*cm, 2.5*cm, 1.5*cm, 3*cm, 2.1*cm, 1.8*cm], style = [
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
# class Reportemov(View):
#     def get(self, *args, **kwargs):
#         hoy = datetime.now()
#         fecha = hoy.strftime("%Y%m%d")
#         response = HttpResponse(content_type='application/pdf')
#         pdf_name = "mov_"+fecha+".pdf"  # llamado clientes
#         # la linea 26 es por si deseas descargar el pdf a tu computadora
#         response['Content-Disposition'] = 'inline; filename=%s' % pdf_name
#         buff = BytesIO()
#         doc = SimpleDocTemplate(buff,
#                                 pagesize=portrait(letter),
#                                 rightMargin=30,
#                                 leftMargin=30,
#                                 topMargin=30,
#                                 bottomMargin=30,
#                                 )

#         cabeza = ParagraphStyle(name="cabeza", alignment=TA_LEFT, fontSize=14, fontName="Times-Roman", textColor=colors.darkblue)
#         cabecera = ParagraphStyle(name="cabecera", alignment=TA_CENTER, fontSize=10, fontName="Times-Roman", textColor=colors.white)
#         celdaderecha = ParagraphStyle(name="celdaderecha",alignment=TA_RIGHT, fontsize=8, fontName="Times-Roman")
#         celdaderechabold = ParagraphStyle(name="celdaderecha",alignment=TA_RIGHT, fontsize=10, fontName="Times-Bold")
#         celda = ParagraphStyle(name="celda", alignment=TA_LEFT, fontsize=8, fontName="Times-Roman")
#         celdabold = ParagraphStyle(name="celda", alignment=TA_LEFT, fontsize=10, fontName="Times-Bold")
#         celdaverde = ParagraphStyle(name="celdaverde", alignment=TA_CENTER, fontSize=8, fontName="Times-Roman", textColor=colors.green)
#         celdaroja = ParagraphStyle(name="celdaroja", alignment=TA_CENTER, fontSize=8, fontName="Times-Roman", textColor=colors.red)
#         celdarojarem = ParagraphStyle(name="celdaroja", alignment=TA_CENTER, fontSize=8, fontName="Times-Roman", textColor=colors.red, backColor = colors.yellow)
#         celdaremarcada = ParagraphStyle(name="celda", alignment=TA_LEFT, fontsize=8, fontName="Times-Roman", backColor=colors.yellow)
#         celdaremarcadader = ParagraphStyle(name="celdader", alignment=TA_RIGHT, fontsize=8, fontName="Times-Roman",
#                                            backColor=colors.yellow)
#         styles = getSampleStyleSheet()
#         styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER, fontSize=16))
#         styles.add(ParagraphStyle(name='subtitulo', alignment=TA_LEFT, fontSize=14))
#         header = Paragraph("Reporte Movimientos "+hoy.strftime("%d/%m/%Y"), styles['centered'])
#         subparticular = Paragraph("Particulares:", styles['Heading2'])
#         subasegurados = Paragraph("Asegurados:", styles['Heading2'])
#         movimiento = []
#         particulares = []
#         asegurados = []
#         total_particular_costo = 0
#         total_particular_cobrado = 0
#         total_asegurado_costo = 0
#         total_particulares = 0
#         total_asegurados = 0
#         movimiento.append(header)
#         movimiento.append(subparticular)
        
#         items = Agendaserv.objects.filter(fecha=datetime.strptime(hoy.strftime("%Y-%m-%d"), "%Y-%m-%d"), agenda__deleted=False)
#         for item in items:
#             if not item.agenda.tipo:
#                 total_particulares = total_particulares + 1
#                 if item.estado:
#                     aux = item.costo
#                     total_particular_cobrado = total_particular_cobrado + item.costo
#                 else:
#                     aux = Decimal('0.00')
#                 if item.descuento:
#                     this_particular = [
#                         Paragraph(str(total_particulares), celda),
#                         Paragraph((item.agenda.paciente.nombres + ' ' + item.agenda.paciente.apellidos), celdaremarcada),
#                         Paragraph(item.servicio.nombre, celdaremarcada), Paragraph(str(item.costo), celdaremarcadader),
#                     ]
#                 else:
#                     this_particular = [
#                         Paragraph(str(total_particulares), celda),
#                         Paragraph((item.agenda.paciente.nombres + ' ' + item.agenda.paciente.apellidos), celda),
#                         Paragraph(item.servicio.nombre, celda), Paragraph(str(item.costo), celdaderecha),
#                     ]
#                 particulares.append(this_particular)
#                 total_particular_costo = total_particular_costo + item.costo
#             else:
#                 total_asegurados = total_asegurados + 1
#                 if item.descuento:
#                     this_asegurado = [
#                         Paragraph(str(total_asegurados), celda),
#                         Paragraph((item.agenda.paciente.nombres+' '+item.agenda.paciente.apellidos), celdaremarcada),
#                         Paragraph(item.servicio.nombre, celdaremarcada), Paragraph(str(item.agenda.procedencia), celdaremarcada),
#                         Paragraph(str(item.costo), celdaremarcadader)
#                     ]
#                 else:
#                     this_asegurado = [
#                         Paragraph(str(total_asegurados), celda),
#                         Paragraph((item.agenda.paciente.nombres + ' ' + item.agenda.paciente.apellidos), celda),
#                         Paragraph(item.servicio.nombre, celda), Paragraph(str(item.agenda.procedencia), celda),
#                         Paragraph(str(item.costo), celdaderecha)
#                     ]
#                 asegurados.append(this_asegurado)
#                 total_asegurado_costo = total_asegurado_costo + item.costo
#         this_particular = [Paragraph('', celda), Paragraph('TOTAL', celdabold), Paragraph('', celda), Paragraph(str(total_particular_costo), celdaderechabold)]
#         particulares.append(this_particular)
#         this_asegurado = [Paragraph('', celda), Paragraph('TOTAL', celdabold), Paragraph('', celda), Paragraph('', celda), Paragraph(str(total_asegurado_costo),celdaderechabold)]
#         asegurados.append(this_asegurado)
#         headings = (Paragraph('Nro', cabecera), Paragraph('Nombre', cabecera), Paragraph('Detalle', cabecera), Paragraph('Costo', cabecera))
#         t1 = Table([headings] + particulares, colWidths=[1 * cm, 10 * cm, 6 * cm, 2 * cm])
#         t1.setStyle(TableStyle(
#         [
#             ('GRID', (0, 0), (6, -1), 1, colors.black),
#             ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
#             ('BACKGROUND', (0, 0), (-1, 0), colors.black)
#         ]
#         ))

#         headings = (Paragraph('Nro', cabecera), Paragraph('Nombre', cabecera), Paragraph('Detalle', cabecera), Paragraph('Procedencia', cabecera), Paragraph('Costo',cabecera))
#         t2 = Table([headings] + asegurados, colWidths=[1 * cm, 7 * cm, 3 * cm, 6 * cm, 2 * cm])
#         t2.setStyle(TableStyle(
#         [
#             ('GRID', (0, 0), (6, -1), 1, colors.black),
#             ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
#             ('BACKGROUND', (0, 0), (-1, 0), colors.black)
#         ]
#         ))


#         movimiento.append(t1)
#         movimiento.append(subasegurados)
#         movimiento.append(t2)
#         doc.build(movimiento)
#         response.write(buff.getvalue())
#         buff.close()
#         return response