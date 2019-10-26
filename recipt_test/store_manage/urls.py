from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.viewStore, name='viewstore'),
    path('regist/', views.regitsStore, name='registstore')
]