from django.shortcuts import render
from .models import Proveedor, Producto

# Funciones CRUD //////////////////////////////////////////////////
# PROVEEDOR
# CREAR PROVEEDOR
def crear_proveedor(request, nombre, apellido, dni):
    nuevo_proveedor = Proveedor.objects.create(
        nombre = nombre,
        apellido = apellido,
        dni = dni
    )
    return render(
        request,
        'nuevo_proveedor.html',
        #HTML ------------- #DJANGO
        {'nuevo_proveedor': nuevo_proveedor}
    )

# MOSTRAR PROVEEDOR
def mostrar_proveedores(request):
    proveedor = Proveedor.objects.all()
    return render(
        request,
        'lista_proveedores.html',
        {'proveedores': proveedor}
    )

# Filtrado de la lista por Apellido
def filtrar_proveedores(request, apellido):
    proveedoresFiltrados = Proveedor.objects.filter(apellido = apellido)
    return render(
        request,
        'proveedores_filtrados.html',
        {'proveedoresFiltrados': proveedoresFiltrados}
    )

# ACTUALIZAR PROVEEDOR por ID
def actualizar_proveedor_id(request, id, nombre, apellido, dni):
    # Acá se identifica al proveedor a cambiar
    proveedor = Proveedor.objects.get(id = id)
    # Acá se hacen los cambios y se reasignan los valores a las nuevas variables
    proveedor.nombre = nombre
    proveedor.apellido = apellido
    proveedor.dni = dni
    # Acá se guardan los cambios
    proveedores = Proveedor.objects.all()
    return render(
        request,
        'lista_proveedores.html',
        {'proveedores': proveedores}
    )

# BORRAR PROVEEDOR
def borrar_proveedor_id(request, id):
    proveedor = Proveedor.objects.get(id = id)
    proveedor.delete()
    # Redirecciono a la lista principal
    proveedores = Proveedor.objects.all()
    return render (
        request,
        'lista_proveedores.html',
        {'proveedores': proveedores}
    )
# Borrar TODA la lista de usuarios
def borrar_todo_proveedores(request):
    proveedores = Proveedor.objects.all()
    proveedores.delete()
    return render(
        request, 
        'lista_proveedores.html',
        {'proveedores': proveedores}
    )



# PRODUCTO REVEER/////////////////////////////////////////////////////////
# CREAR PRODUCTO
def crear_producto(request, nombre, precio, stock_actual, proveedor):
    nuevo_producto = Producto.objects.create(
        nombre = nombre,
        precio = precio,
        stock_actual = stock_actual,
        proveedor = proveedor
    )
    return render(
        request,
        'nuevo_producto.html',
        #HTML ------------- #DJANGO
        {'nuevo_producto': nuevo_producto}
    )


# MOSTRAR PRODUCTO
def mostrar_productos(request):
    producto = Producto.objects.all()
    return render(
        request,
        'lista_productos.html',
        {'productos': producto}
    )

# Filtrado de la lista por Nombre
def filtrar_productos(request, nombre):
    productosFiltrados = Producto.objects.filter(nombre = nombre)
    return render(
        request,
        'productos_filtrados.html',
        {'productosFiltrados': productosFiltrados}
    )
 
# ACTUALIZAR PRODUCTO por ID
def actualizar_producto_id(request, id, nombre, precio, stock_actual, proveedor):
    # Acá se identifica al proveedor a cambiar
    producto = Producto.objects.get(id = id)
    # Acá se hacen los cambios y se reasignan los valores a las nuevas variables
    producto.nombre = nombre
    producto.precio = precio
    producto.stock_actual = stock_actual
    # Acá se guardan los cambios
    productos = Producto.objects.all()
    return render(
        request,
        'lista_productos.html',
        {'productos': productos}
    )
# BORRAR PRODUCTO
def borrar_producto_id(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    # Redirecciono a la lista principal
    productos = Producto.objects.all()
    return render (
        request,
        'lista_productos.html',
        {'productos': productos}
    )
# Borrar TODA la lista de usuarios
def borrar_todo_productos(request):
    productos = Producto.objects.all()
    productos.delete()
    return render(
        request, 
        'lista_productos.html',
        {'productos': productos}
    )
