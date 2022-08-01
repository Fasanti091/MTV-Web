from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Familiares
from django.template import Template, Context, loader

# Create your views here.

def index(request):

    

    familiares = Familiares.objects.all()

    familiares = {'familiares':familiares}

    plantilla = loader.get_template("index.html")

    documento = plantilla.render(familiares)

    return HttpResponse(documento)
