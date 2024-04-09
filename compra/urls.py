from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #URL ADMIN
    path('admin/', admin.site.urls),
    #URL Index/Home
    path('', views.index, name="Inicio"),
    path('indexinvitado', views.index2, name="Inicio de Invitado"),

    #URLS Proveedores
    path('creacionproveedor/', views.crear_proveedor),
    path('listaproveedores', views.mostrar_proveedores, name="Mostrar Proveedores"),
    path('filtroproveedor', views.filtrar_proveedores, name="Filtrar Proveedores por Apellido"),    
    path('actualizarproveedor/<int:id>/<str:nombre>/<str:apellido>/<int:dni>', views.actualizar_proveedor_id, name = "Actualizar Proveedores por Id"),
    path('eliminarproveedor/<int:id>', views.borrar_proveedor_id, name="Borrar Proveedor por Id"),
    path('eliminarproveedores', views.borrar_todo_proveedores, name="Borrar todos los Proveedores"),

    #URLS Productos
    path('creacionproducto/', views.crear_producto),
    path('listaproductos', views.mostrar_productos, name="Mostrar Productos"),
    path('filtroproducto', views.filtrar_productos, name="Filtrar producto por Nombre"),    
    path('actualizarproducto/<str:nombre>/<int:precio>/<int:stock_actual>', views.actualizar_producto_id, name = "Actualizar Producto por Id"),
    path('eliminarproducto/<int:id>', views.borrar_producto_id, name="Borrar Producto por Id"),
    path('eliminarproductos', views.borrar_todo_productos, name="Borrar todos los Productos"),

]
