from django.urls import path
from . import views

app_name = "fileupload"

urlpatterns = [
    path('pfile/',views.dfile,name="pfile"),
    path('pupload/',views.dupload,name="pupload")
]
