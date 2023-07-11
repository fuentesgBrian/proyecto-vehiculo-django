from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Vehiculo

from .forms import UserRegisterForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    return render(request, 'vehiculo/index.html')

@login_required(login_url='/login/')
@permission_required(perm='can_add_vehiculo', login_url='/login/')
def add(request):
    return render(request, 'vehiculo/agregarvehiculo.html')

def vehiculoadd(request):
    print(request.POST)
    marca = request.POST['marca']
    modelo = request.POST['modelo']
    serial_carro = request.POST['serial_carro']
    serial_motor = request.POST['serial_motor']
    categoria = request.POST['categoria']
    precio = request.POST['precio']
    vehiculo = Vehiculo(marca=marca, modelo=modelo, serial_carro=serial_carro, serial_motor=serial_motor, categoria=categoria, precio=precio)
    vehiculo.save()
    return HttpResponseRedirect('/vehiculo/list')

@permission_required(perm='vehiculo.visualizar_catalogo', login_url='/login/')
def listarvehiculo(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'vehiculo/listarvehiculo.html', context)


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Vehiculo)
            visualizar_catalogo = Permission.objects.get(
                codename='visualizar_catalogo',
                content_type=content_type
            )
            user = form.save()
            #Permite el funcionamiento del checkbox
            user.user_permissions.add(visualizar_catalogo)
            if form.cleaned_data['add_vehiculomodel']:
                permission = Permission.objects.get(
                    codename='add_vehiculomodel')
                user.user_permissions.add(permission)
                user.is_staff = True
                user.is_superuser = True
                user.save()

            login(request, user)
            messages.success(request, "registrado satisfactoriamente")
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
        return HttpResponseRedirect('/')

    form = UserRegisterForm()
    context = {'register_form':form}
    return render(request, "vehiculo/registro.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"username o password incorrectos.")
                return HttpResponseRedirect('/login')
        else:
            messages.error(request, "username o password incorrectos.")
            return HttpResponseRedirect('/login')
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request, 'vehiculo/login.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesion satisfactoriamente.")
    return HttpResponseRedirect('/')