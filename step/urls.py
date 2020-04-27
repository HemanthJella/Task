from django.contrib import admin
from django.urls import path, include
from step import views

urlpatterns = [
    path('', views.index, name="index"),
    path('choose/', views.choose, name="choose"),
    path('ask/', views.ask, name="ask"),   
]