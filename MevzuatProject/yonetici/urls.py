
from django.urls import path
from.import views

app_name = "yonetici"

urlpatterns = [
    path('register1/', views.register, name="register1"),
    path('login1/', views.loginUser, name="login1"),
    path('logout/', views.logoutUser, name="logout"),
    ]
