from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('generate/<int:ser>/<int:col>/', views.generate, name='generate'),
    path('rnd/', views.rnd, name='rnd'),
    path('list/', views.list, name='list'),
    path('info/', views.info, name='info'),
    path('balance/<int:id_card>/', views.balance, name='balance'),
    path('status/<int:id_card>/', views.status, name='status'),
    path('delete/<int:id_card>/', views.delete, name='delete'),
]
