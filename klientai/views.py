from django.shortcuts import render
from django.http import Http404

from .models import Klientas

def sarasas(request):
    visi_klientai = Klientas.objects.all()
    return render(request, 'klientu_sarasas.html', {'klientai': visi_klientai})


def issamiau(request, pk):
    try:
        klientas = Klientas.objects.get(pk=pk)
    except Klientas.DoesNotExist:
        raise Http404('Tokio kliento nera')
    return render(request, 'klientai_issamiau.html', {'klientas': klientas})

