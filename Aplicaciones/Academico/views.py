from django.shortcuts import render, redirect
from .models import Curso



from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from io import BytesIO
from reportlab.platypus import Image

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.colors import black

def reporte(request, codigo):
    curso = Curso.objects.get(codigo=codigo)

    response = HttpResponse(content_type'aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename-Platzi-student-report.pdf'
    buffer = bytesID()

    c = canvas.Canvas(buffer, pagesize=latter)
    c.setLineWidth(.3)
    c.line(460,747,560,747)
    c.setFillColor(black)
    c.drawImage("/static/css/imagen/ojo.jpeg", -25,40)
    c.setFont('Helvetica',16)
    c.drawString(105,365,curso.nombre.strip())
    c.drawString(105,240,curso.creditos.strip())
    c.showPage()
    c.save()

    pdf=buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
# Create your views here.


def inicio(request):
    cursosListados = Curso.objects.all()
    #messages.success(request, '¡Cursos listados!')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def talleres(request):
    return render(request, 'talleres.html')

def nuevo(request):
    return render(request, 'nuevo.html')

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    
    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    #messages.success(request, '¡Curso registrado!')
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    
    return redirect('/')
    
    
def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    
    return redirect('/')