from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.viewStore, name='viewstore'),
    path('regist/', views.registrecipt, name='registrecipt'),
    path('delete/<int:re_id>', views.delete, name='delete')
]