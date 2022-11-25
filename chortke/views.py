from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HomeWebPage(request):
    '''in this class we say Hello to World'''
    return HttpResponse('Hello World!')