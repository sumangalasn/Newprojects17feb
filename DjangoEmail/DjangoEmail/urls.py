from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url('send-email', EmailAPI.as_view()),
]