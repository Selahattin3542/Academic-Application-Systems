from django.urls import path
from . import views

app_name = "yardimci"

urlpatterns = [
    path('yard_formu/',views.yardimci,name="yard_formu"),
    ]
