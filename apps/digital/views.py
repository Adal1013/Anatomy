from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from apps.digital.models import Organo, Parte
# Create your views here.
def home(request):
    organos = Organo.objects.all()
    context = {"organos": organos}
    return render(request, 'contenido/home.html', context)

def organo(request, pk):
    organo = Organo.objects.get(id=pk)
    context = {"organo": organo}
    return render(request, 'contenido/organo.html', context)
