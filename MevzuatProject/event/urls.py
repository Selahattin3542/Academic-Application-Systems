from django.urls import path
from . import views

urlpatterns = [
    path('add_event/',views.event_ekle, name='add_events'),
    path('liste/',views.etkinlik_listesi,name="liste")
]


