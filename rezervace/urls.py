from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznam', views.RezervaceListView.as_view(), name='seznam_rezervaci'),
    path('detail/<int:pk>', views.RezervaceDetailView.as_view(), name='detail_rezervace'),
]
