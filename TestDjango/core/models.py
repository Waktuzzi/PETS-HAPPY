from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreCategoria

class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20, null=False)
    marca = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True)
    precio = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.nombre+" "+self.id

class Historial(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField(null=False)
    cantidad = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.nombre+" "+self.id

class Ofertas(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descuento = models.CharField(max_length=2, null=False)

    def __str__(self) -> str:
        return self.nombre+" "+self.id

