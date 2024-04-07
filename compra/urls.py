from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #URL ADMIN
    path('admin/', admin.site.urls),
    #URLS Proveedores
    path('crearproveedor/<str:nombre>/<str:apellido>/<int:dni>', views.crear_proveedor, name="Crear Proveedor"),
    path('', views.mostrar_proveedores, name="Mostrar Proveedores"),
    path('filtroproveedor', views.filtrar_proveedores, name="Filtrar Proveedores por Apellido"),    
    path('actualizarproveedor/<int:id>/<str:nombre>/<str:apellido>/<int:dni>', views.actualizar_proveedor_id, name = "Actualizar Proveedores por Id"),
    path('eliminarproveedor/<int:id>', views.borrar_proveedor_id, name="Borrar Proveedor por Id"),
    path('eliminarproveedores', views.borrar_todo_proveedores, name="Borrar todos los Proveedores"),
    #URLS Productos
    path('crearproducto/<str:nombre>/<int:precio>/<int:stock_actual>', views.crear_producto, name="Crear Producto"),
    path('', views.mostrar_productos, name="Mostrar Productos"),
    path('filtroproducto', views.filtrar_productos, name="Filtrar producto por Nombre"),    
    path('actualizarproducto/<str:nombre>/<int:precio>/<int:stock_actual>', views.actualizar_producto_id, name = "Actualizar Producto por Id"),
    path('eliminarproducto/<int:id>', views.borrar_producto_id, name="Borrar Producto por Id"),
    path('eliminarproductos', views.borrar_todo_productos, name="Borrar todos los Productos"),
]
