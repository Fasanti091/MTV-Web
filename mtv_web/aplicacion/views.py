from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Familiares
from django.template import Template, Context, loader
from datetime import datetime

# Create your views here.

def index(request):

    # Traemos la base de datos
    familiares = Familiares.objects.all()
    
    # Creamos un contexto
    contexto = {'familiares':familiares,"datetime": datetime.now()}
    
    # Llamamos a index
    plantilla = loader.get_template("index.html")

    # Ponemos el contexto en el index para poder usarlo
    documento = plantilla.render(contexto)

    # Retornamos los archivos
    return HttpResponse(documento)
