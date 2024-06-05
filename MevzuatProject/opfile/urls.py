from django.urls import path
from . import views

app_name = "fileupload"

urlpatterns = [
    path('opfile/',views.dfile,name="opfile"),
    path('opupload/',views.dupload,name="oupload")
]
