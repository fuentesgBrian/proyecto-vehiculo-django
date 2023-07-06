from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('vehiculo/add/', views.add, name='add'),
    path('vehiculo/add/url/', views.vehiculoadd, name='vehiculoadd')
]
