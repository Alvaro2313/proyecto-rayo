from django.shortcuts import render , redirect

from .models import Cliente
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required
def proyecto(request):
    context={}
    return render(request, 'tallerdb/proyecto.html', context)

def salir (request):
    logout(request)
    return redirect('/')

def index(request):
    return render(request,'tallerdb/paginacargaini.html')

def cambiomotor(request):
    return render(request, 'tallerdb/cambiodemotor.html')

def formulario(request):
    return render(request, 'tallerdb/formulario.html')

def equipo(request):
    return render(request, 'tallerdb/equipo.html')

def correo(request):
    return render(request, 'tallerdb/correo.html')

def inicio(request):
    return render(request, 'registration/login.html')
def edifor(request):
    return render(request, 'tallerdb/edicionfor.html')


def home(request):
    clientes = Cliente.objects.all()
    messages.success(request, '¡Clientes listados!')
    return render(request, 'tallerdb/clientes.html',{"clientes":clientes})
def registrarCliente(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellido_paterno = request.POST['apellido_paterno']
    apellido_materno = request.POST['apellido_materno']
    telefono = request.POST['telefono']
    email = request.POST['email']
    direccion = request.POST['direccion']
    activo = request.POST['activo']
    cliente = Cliente.objects.create(rut=rut, nombre=nombre, apellido_paterno=apellido_paterno,
                                     apellido_materno=apellido_materno,telefono=telefono,email=email,direccion=direccion,activo=activo)
    messages.success(request, '¡Cliente registrado!')
    return redirect('formulario')

def edicionCliente(request, rut):
    cliente = Cliente.objects.get(rut=rut)
    return render(request, "tallerdb/edicionfor.html", {"cliente": cliente})

def editarCliente(request):
    rut = request.POST['rut']
    nombre=request.POST['nombre']
    apellido_paterno = request.POST['apellido_paterno']
    apellido_materno = request.POST['apellido_materno']
    telefono = request.POST['telefono']
    email = request.POST['email']
    direccion = request.POST['direccion']
    activo = request.POST['activo']
    cliente=Cliente.objects.get(rut=rut)
    cliente.rut=rut
    cliente.nombre=nombre
    cliente.apellido_paterno=apellido_paterno
    cliente.apellido_materno=apellido_materno
    cliente.telefono=telefono
    cliente.email=email
    cliente.direccion=direccion
    cliente.activo=activo
    cliente.save()
    return redirect('/')

def eliminarCliente(request, rut):
    cliente = Cliente.objects.get(rut=rut)
    cliente.delete()

    messages.success(request, '¡Cliente eliminado!')

    return redirect('/')
