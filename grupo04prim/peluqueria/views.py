from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def quienessomos(request):
	return render(request, 'quienessomos.html')

def servicios(request):
	return render(request, 'servicios.html')

def reservahora(request):
	return render(request, 'reservahora.html')	

def contacto(request):
	return render(request, 'contacto.html')

def registro(request):
	return render(request, 'registro.html')

def iniciarsesion(request):
	return render(request, 'iniciarsesion.html')		

def recup1(request):
	servicio=request.POST["inputservicio"] 
	profesional=request.POST["inputprofesional"]
	dia=request.POST["inputfecha"]
	hora=request.POST["inputhora"]
	nombre=request.POST["inputnombre"]
	apellido=request.POST['inputapellido']
	telefono=request.POST["inputtelefono"]
	email=request.POST["inputemail"]
	diccionario={}
	diccionario["serv"]=servicio
	diccionario["prof"]=profesional
	diccionario["date"]=dia
	diccionario["hour"]=hora
	diccionario["name"]=nombre
	diccionario["lastname"]=apellido
	diccionario["fono"]=telefono
	diccionario["mail"]=email
	return render(request, "resultadoreserva.html", diccionario)	

def recup2(request):
	nombre=request.POST["inputnombre"]
	diccionario={}
	diccionario["name"]=nombre
	return render(request, "resultadocontacto.html", diccionario)

def recup3(request):
	nombre=request.POST["inputnombre"]
	apellido=request.POST['inputapellido']
	telefono=request.POST["inputtelefono"]
	email=request.POST["inputemail"]
	diccionario={}
	diccionario["name"]=nombre
	diccionario["lastname"]=apellido
	diccionario["fono"]=telefono
	diccionario["mail"]=email
	return render(request, "resultadoregistro.html", diccionario)

def recup4(request):
	email=request.POST["inputemail"]
	diccionario={}
	diccionario["mail"]=email
	return render(request, "resultadoiniciarsesion.html", diccionario)					