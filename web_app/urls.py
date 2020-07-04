from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name = "login_page"),
    path('reg/',views.reg_page,name = "reg_page"),
    path('dashboard/', views.dashboard, name='dashboard'),
]