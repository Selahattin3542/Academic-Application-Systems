from django.urls import path
from . import views

app_name = "fileupload"

urlpatterns = [
    path('file_upload/',views.upload_file,name="file_upload"),
    path('upload/',views.dosya_listesi,name="upload")

    ]
