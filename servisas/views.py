from django.shortcuts import render
from django.http import HttpResponse


def pradinis(request):
#    return HttpResponse("Hello, world. You're at the registracija page.")
    return render(request, 'pradinis.html')

