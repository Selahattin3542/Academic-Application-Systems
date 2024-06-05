from django.urls import path
from . import views

app_name = "akategori"

urlpatterns = [
    path('kategori_puan/',views.create_category,name="kategori_puan"),

    ]
