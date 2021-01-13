from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return render(request, 'bienvenido.html')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contactar(request):
    return HttpResponse('<p>Email: Blabla@bla.com</p><p>Telefono:555-555-555</p>')