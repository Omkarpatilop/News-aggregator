from django.contrib import admin
from django.urls import path
from newsApp.views import *

urlpatterns = [
    path('',index,name="index"),]
