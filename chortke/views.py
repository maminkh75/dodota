from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
import json
from chortke.models import User,Expense,Token,Income
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt

# class HomeWebPage(TemplateView):
#     '''in this class we say Hello to World'''
#     template_name="home.html"

def submit_expenses(request):

    this_token=request.POST['token']
    this_user=User.objects.filter(token__token=this_token).get()

    if 'date' not in request.POST:
        date=datetime.datetime.now()
    Expense.objects.create(user=this_user,amount=request.POST['amount'],
                           text=request.POST['text'],date=date)        
    return JsonResponse({
        'status':'OK'},encoder=json.JSONEncoder)