from django.shortcuts import render
from .models import Ubytovani


def index(request):
    context = {
        'nadpis': 'Ubytovací zařízení',
        'mista': Ubytovani.objects.filter(pocet_pokoju__gt = 2)
    }
    return render(request, 'index.html', context=context)
