"""MevzuatProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
from django.contrib import admin
from django.urls import path, include

from article import views as article_views
from basvuru import views as basvuru_views
from yardimci import views as yardimci_views
from YDS import views as YDS_views
from profesor import views as profesor_views
from django.conf import settings
from django.conf.urls.static import static
from ondocent import views as ondocent_views
from onprof import views as onprof_views
from makale import views as makale_views
from onyard import views as onyard_views
from fileupload import views as file_views
from form import views as form_views
from yonetmelik import views as yonetmelik_views
from event import views as event_views
from dfile import  views as dfile_views
from drfile import views as drfile_views
from odfile import views as odfile_views
from odrfile import views as odrfile_views
from opfile import  views as opfile_views
from pfile import views as pfile_views
from kullanici import views as k_views
from akategori import views as a_views
from  bkategori import views as b_views
from  ckategori import views as c_views
from  dkategori import views as d_views


urlpatterns = [
 path('admin/', admin.site.urls),
 path('', article_views.index, name="index"),
 path('about/', article_views.about, name="about"),
 path('articles/', include("article.urls")),
 path('user/', include("user.urls")),
 path('user2/',include("user2.urls")),
 path('basvuru/', basvuru_views.basvuru, name="basvuru_formu"),
 path('yardimci/',yardimci_views.basvuru, name="yard_formu"),
 path('YDS/',YDS_views.indir_belge, name="yds_sonuc_belge"),
 path('profesor/',profesor_views.basvuru,name="prof_formu"),
 path('ondocent/',ondocent_views.ondocent_view,name="ondocent_form"),
 path('onprof/',onprof_views.prof_view,name="onprof_form"),
 path('makale/',makale_views.download_article,name="makale"),
 path('onyard/',onyard_views.onyard_view,name="onyard_formu"),
 path('fileupload/', file_views.upload_file, name='file_upload'),
 path('form/',form_views.indir_belge_form,name="form"),
 path('yonetmelik/',yonetmelik_views.yonetmelik_yonlendir,name="yonetmelik"),
 path('event/add_event/',event_views.event_ekle,name="add_events"),
 path('event/liste/',event_views.etkinlik_listesi,name="liste"),
 path('fileupload/file_upload/',file_views.upload_file,name="file_upload"),
 path('fileupload/upload/',file_views.dosya_listesi,name="upload"),
 path('dfile/dfile/',dfile_views.dfile,name="dfile"),
 path('dfile/dupload/',dfile_views.dupload,name="dupload"),
 path('drfile/drfile/',drfile_views.dfile,name="drfile"),
 path('drfile/drupload/',drfile_views.dupload,name="drupload"),
 path('odfile/odfile/',odfile_views.dfile,name="odfile"),
 path('odfile/odupload/',odfile_views.dupload,name="odupload"),
 path('odrfile/odrfile/',odrfile_views.dfile,name="odrfile"),
 path('odrfile/odrupload/',odrfile_views.dupload,name="odrupload"),
 path('opfile/opfile/',opfile_views.dfile,name="opupload"),
 path('opfile/opupload/',opfile_views.dupload,name="dupload"),
 path('pfile/pfile/',pfile_views.dfile,name="pfile"),
 path('pfile/pupload/',pfile_views.dupload,name="pupload"),
 path('akategori/',a_views.create_category,name="kategori_puan"),
 path('bkategori/',b_views.create_category,name="kategori_puan"),
 path('ckategori/',c_views.create_category,name="kategori_puan"),
 path('dkategori/',d_views.create_category,name="kategori_puan"),
 path('kullanici/login1/',k_views.loginUser,name="login1"),
path('kullanici/register1/',k_views.register,name="register1"),
path('kullanici/logout/',k_views.logoutUser,name="logout"),


       ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




