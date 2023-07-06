from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Vehiculo
# Create your views here.

def index(request):
    return render(request, 'vehiculo/index.html')

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
    return HttpResponseRedirect('/vehiculo/add')