from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Familiares
from django.template import Template, Context, loader
from datetime import datetime

# Create your views here.

def index(request):


    familiares = Familiares.objects.all()

    contexto = {'familiares':familiares,"datetime": datetime.now()}

    plantilla = loader.get_template("index.html")

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
