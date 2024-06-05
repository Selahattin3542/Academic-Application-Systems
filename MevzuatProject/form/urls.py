from django.urls import path
from .import views

urlpatterns = [

    path('form/', views.indir_belge_form, name='form'),

]
