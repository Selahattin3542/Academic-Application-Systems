from django.urls import path
from . import views

app_name = "profesor"

urlpatterns = [
    path('profesor/prof_form/',views.basvuru,name="prof_formu"),
    path('profesor/basvuru_liste/',views.basvuru_listesi,name="basvuru_liste")
    ]
