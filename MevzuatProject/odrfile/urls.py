from django.urls import path
from . import views

app_name = "fileupload"

urlpatterns = [
    path('odrfile/',views.dfile,name="odrfile"),
    path('odrupload/',views.dupload,name="odrupload")
]
