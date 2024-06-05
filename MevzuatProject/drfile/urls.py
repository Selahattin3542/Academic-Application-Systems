from django.urls import path
from . import views

app_name = "fileupload"

urlpatterns = [
    path('drfile/',views.dfile,name="drfile"),
    path('drupload/',views.dupload,name="drupload")

    ]
