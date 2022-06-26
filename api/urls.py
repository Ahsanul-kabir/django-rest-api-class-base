import django
from django import urls


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('data-view/<int:pk>/', views.dataView, name='dataview'),
    path('data-add', views.dataAdd, name='dataadd'),
    path('update-data/<int:pk>/', views.dataUpdate, name='dataupdate'),
    path('delete-data/<int:pk>/', views.datadelete, name='datadelete'),
]
