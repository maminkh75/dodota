from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class HomeWebPage(TemplateView):
    '''in this class we say Hello to World'''
    template_name="home.html"