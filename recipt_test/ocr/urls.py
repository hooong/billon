from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('submit/<int:re_id>', views.submit_img, name='submit'),
    path('read/<int:re_id>', views.ocr_test, name='ocr')
]