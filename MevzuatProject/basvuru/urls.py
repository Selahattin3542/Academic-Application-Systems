
from django.contrib import admin
from django.urls import path,include
from.import views

app_name = "basvuru"

urlpatterns = [
    path('basvuru_formu/', views.basvuru, name="basvuru_formu"),
]

