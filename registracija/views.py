from django.shortcuts import render
from django.http import HttpResponse


def registracija(request):
#    return HttpResponse("Hello, world. You're at the registracija page.")
    return render(request, 'registracija.html')

def pradinis(request):
#    return HttpResponse("Hello, world. You're at the registracija page.")
    return render(request, 'pradinis.html')

