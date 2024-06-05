from django.urls import path
from . import views

app_name = "fileupload"

urlpatterns = [
    path('dfile/',views.dfile,name="dfile"),
    path('dupload/',views.dupload,name="dupload")

    ]
