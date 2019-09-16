from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('pelomalo/', quienessomos, name='quienessomos'),
	path('servicios/', servicios, name='servicios'),
	path('reserva/', reservahora, name='reservahora'),
	path('contacto/', contacto, name='contacto'),
	path('registro/', registro, name='registro'),
	path('iniciarsesion/', iniciarsesion, name='iniciarsesion'),
	path('resultadoreserva', recup1, name='resultadoreserva'),
	path('resultadocontacto', recup2, name='resultadocontacto'),
	path('resultadoregistro', recup3, name='resultadoregistro'),
	path('resultadoiniciarsesion', recup4, name='resultadoiniciarsesion'),
	
	
]