from django.urls import path
from rest_producto.viewsLogin import Login, Login
from .views import *

urlpatterns = [
    path('VariosProductos', VariosProductos, name="VariosProductos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('Login', Login, name="Login"),
]

