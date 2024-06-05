from django.urls import path
from .import views

urlpatterns = [

    path('yonetmelik/', views.yonetmelik_yonlendir, name='yonetmelik'),

]
