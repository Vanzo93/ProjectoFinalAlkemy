from django.contrib import admin
# Se agrega el 'include' para incluir las urls de la app en el proyecto
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('compra.urls'))
]
