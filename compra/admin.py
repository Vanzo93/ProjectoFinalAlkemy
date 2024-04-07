from django.contrib import admin
from .models import Proveedor, Producto


# Panel de ADMIN

class ProveedorAdmin(admin.ModelAdmin):
    # 1° propiedad: Permite que aparezcan los nombres de las columnas de los productos.
    # Sin esto, cada item de la clase producto se vería como "Producto Object(1)"
    list_display = ['id', 'nombre', 'apellido', 'dni']
    # 2° propiedad: Agrega un cuadro de búsqueda, dependiendo de lo que se ponga dentro del search_fields,
    # buscará por determinada característica.
    search_fields = ['id', 'nombre', 'apellido', 'dni']


# Lo mismo hago para Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'stock_actual', 'proveedor']
    search_fields = ['id', 'nombre', 'precio', 'stock_actual']


# Agrego la línea de código para vincular los modelos con el Admin
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)

