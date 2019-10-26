from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('submit/', views.submit_img, name='submit'),
    path('read/', views.ocr_test, name='ocr')
]