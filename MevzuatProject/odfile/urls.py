from django.urls import path
from . import views

app_name = "fileupload"

urlpatterns = [
    path('odfile/',views.dfile,name="odfile"),
    path('odupload/',views.dupload,name="odupload")
]
