from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage, name='mainpage_url'),
]
