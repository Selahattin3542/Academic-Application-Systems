
from django.urls import path
from.import views

app_name = "user2"

urlpatterns = [
    path('register1/', views.register1, name="register1"),
    path('login1/', views.loginUser1, name="login1"),
    path('logout1/', views.logoutUser1, name="logout1"),
    ]
