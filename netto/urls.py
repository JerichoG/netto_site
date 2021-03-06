from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('configt/', views.configt, name='configt'),
    path('deviceslist/', views.deviceslist, name='deviceslist'),
    path('log/', views.log, name='log'),
    path('saveconf/', views.saveconf, name='saveconf'),
    path('pinging/', views.pinging, name='pinging'),
    path('verifcli/<int:id>', views.verifcli),
]
