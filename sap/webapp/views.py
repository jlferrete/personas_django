from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):

    no_personas_var = Persona.objects.count()

    return render(request, 'bienvenido.html', {'no_personas':no_personas_var})

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contactar(request):
    return HttpResponse('<p>Email: Blabla@bla.com</p><p>Telefono:555-555-555</p>')