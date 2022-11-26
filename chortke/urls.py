from django.urls import path
from .views import HomeWebPage

urlpatterns=[
    path("",HomeWebPage.as_view(),name='home'),
    ]