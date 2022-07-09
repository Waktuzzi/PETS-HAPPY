from re import template
from xml.etree.ElementInclude import include
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('crearProducto', crearProducto, name="crearProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('elimirnarProducto/<id>', elimirnarProducto, name="elimirnarProducto"),
    path('modificarOferta/<id>', modificarOferta, name="modificarOferta"),
    path('elimirnarOferta/<id>', elimirnarOferta, name="elimirnarOferta"),
    path('elimirnarCompra/<id>', elimirnarHistorial, name="elimirnarCompra"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('aves', aves, name="aves"),
    path('gatos', gatos, name="gatos"),
    path('peces', peces, name="peces"),
    path('perros', perros, name="perros"),
    path('crud', crud, name="crud"),
    path('registro', registro, name="registro"),
    path('donar', donar, name="donar"),
    path('añadirCompra', añadirCompra, name="añadirCompra"),
    path('crearOferta', crearOferta, name="crearOferta"),
    path('historialCompra', historialCompra, name="historialCompra"),
    path('oferta', oferta, name="oferta"),
    path('pago', pago, name="pago"),
]
