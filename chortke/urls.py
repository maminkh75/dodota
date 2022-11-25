from django.urls import path
from .views import HomeWebPage

urlpatterns=[
    path("",HomeWebPage,name='home'),
    ]