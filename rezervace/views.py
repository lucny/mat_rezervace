from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Ubytovani, Rezervace


def index(request):
    context = {
        'nadpis': 'Ubytovací zařízení',
        'mista': Ubytovani.objects.filter(pocet_pokoju__gt = 2)
    }
    return render(request, 'index.html', context=context)


class RezervaceListView(ListView):
    model = Rezervace
    template_name ='rezervace/list.html'
    context_object_name ='rezervace_list'
    queryset = Rezervace.objects.order_by('ubytovani')


class RezervaceDetailView(DetailView):
    model = Rezervace
    template_name ='rezervace/detail.html'
    context_object_name ='rezervace'

