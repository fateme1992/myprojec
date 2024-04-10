from django.contrib import admin
from django.urls import path
from mysite.views import index

app_name='mysite'

urlpatterns = [
    path('',index),
]
