from django.urls import path
from .import views

urlpatterns = [

    path('yds_sonuc_belge/', views.indir_belge, name='yds_sonuc_belge'),

]
