from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos 
from django.conf import settings
from django.core.mail import send_mail
from gestionPedidos.forms import Formulario_Contacto

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
       # mensaje="Artículo buscado: %r" %request.GET["prd"]
       producto=request.GET["prd"]

       if len(producto)>20:

            mensaje="Texto demasiado largo"

       else:

            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request,"resultados_busquedas.html",{"articulos":articulos,"query":producto})

    else:

        mensaje="Tiene que buscar un producto"

        
    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":

        mi_Formulario=Formulario_Contacto(request.POST)

        if mi_Formulario.is_valid():

            inf_Form=mi_Formulario.cleaned_data

            send_mail(inf_Form['asunto'], inf_Form['mensaje'], inf_Form.get('email',''),['juliomederosarias@gmail.com'],)

            return render(request,"gracias.html")

        else:

            return render(request,"algo_mal.html")

    else:

        mi_Formulario= Formulario_Contacto()

    return render(request, "contacto.html", {"form":mi_Formulario})

   