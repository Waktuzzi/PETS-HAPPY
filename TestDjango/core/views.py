from ast import If
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def registro(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form':form})


def crud(request):
    contexto = {'Productos': Producto.objects.all(), 'Ofertas': Ofertas.objects.all()}
    return render(request, 'core/crud.html', contexto)
def pago(request):
    return render(request, 'core/pago.html')
def aves(request):
    return render(request, 'core/aves.html')
def gatos(request):
    return render(request, 'core/gatos.html')
def peces(request):
    return render(request, 'core/peces.html')
def perros(request):
    return render(request, 'core/perros.html')
def home(request):
    return render(request, 'core/home.html')
def donar(request):
    return render(request, 'core/subscripciones.html')
def historialCompra(request):
    contexto = {'Historial': Historial.objects.all()}
    return render(request, 'core/historialCompra.html',contexto)


def crearProducto(request):
    contexto = {'form': ProductosForm()}
    if request.method == "POST":
        Producto = ProductosForm(request.POST)
        if Producto.is_valid:
            Producto.save()
            contexto["mensaje"] = "Producto Agregado"
    return render(request, 'core/crearProducto.html', contexto)

def modificarProducto(request, id):
    fernando = Producto.objects.get(id=id)
    datos = {'form': ProductosForm(instance=fernando)}
    if request.method == "POST":
        form = ProductosForm(request.POST, instance=fernando)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/crearProducto.html', datos)

def elimirnarProducto(request, id):
    joder = Producto.objects.get(id=id)
    joder.delete()
    return redirect(to="crud")

def añadirCompra(request):
    contexto = {'form': HistorialForm()}
    if request.method == "POST":
        Producto = HistorialForm(request.POST)
        if Producto.is_valid:
            Producto.save()
            contexto["mensaje"] = "Producto Agregado"
    return render(request, 'core/añadirCompra.html', contexto)

def crearOferta(request):
    contexto = {'form': OfertasForm()}
    if request.method == "POST":
        Producto = OfertasForm(request.POST)
        if Producto.is_valid:
            Producto.save()
            contexto["mensaje"] = "Oferta Agregado"
    return render(request, 'core/crearOferta.html', contexto)

def modificarOferta(request, id):
    fernando = Ofertas.objects.get(id=id)
    datos = {'form': OfertasForm(instance=fernando)}
    if request.method == "POST":
        form = OfertasForm(request.POST, instance=fernando)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/crearProducto.html', datos)

def elimirnarOferta(request, id):
    joder = Ofertas.objects.get(id=id)
    joder.delete()
    return redirect(to="crud")

def elimirnarHistorial(request, id):
    joder = Historial.objects.get(id=id)
    joder.delete()
    return redirect(to="historialCompra")

def oferta(request):
    posts = Ofertas.objects.all()
    return render(request, 'core/ofertas.html',{"posts": posts})