from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    mensajes = {'msg1':'Valor mensaje 1', 'msg2':'Valor mensaje 2'}
    return render(request, 'bienvenido.html', mensajes)

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contactar(request):
    return HttpResponse('<p>Email: Blabla@bla.com</p><p>Telefono:555-555-555</p>')