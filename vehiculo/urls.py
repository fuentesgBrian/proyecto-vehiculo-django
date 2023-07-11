from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('vehiculo/add/', views.add, name='add'),
    path('vehiculo/add/url/', views.vehiculoadd, name='vehiculoadd'),
    path('vehiculo/list/', views.listarvehiculo, name='listarvehiculo'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
