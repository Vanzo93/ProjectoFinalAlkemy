from django.db import models

# Creamos modelo PROVEEDOR
class Proveedor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    dni = models.IntegerField(max_length=10)
    # Quiero que figure no solamente el nombre, sino también el apellido del proveedor
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

        


# Creamos modelo PRODUCTO en donde tiene su campo PROVEEDOR dependiendo de la clase anterior mencionada
class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.FloatField(max_length=15)
    stock_actual = models.IntegerField(max_length=10)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True )
    def __str__(self):
        return self.nombre