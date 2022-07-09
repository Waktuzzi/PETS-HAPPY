from pyexpat import model
from django.forms import ModelForm
from .models import *
class ProductosForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id','nombre','marca','categoria','stock','precio']

class HistorialForm(ModelForm):
    class Meta:
        model = Historial
        fields = ['id','nombre','precio','cantidad']

class OfertasForm(ModelForm):
    class Meta:
        model = Ofertas
        fields = ['id','nombre','descuento']