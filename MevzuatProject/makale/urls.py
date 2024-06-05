from django.urls import path
import views

urlpatterns = [
    path('download_article/', views.download_article, name='download_article'),
]
