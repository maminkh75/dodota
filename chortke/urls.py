from django.urls import path
from .views import submit_expenses


urlpatterns=[
    #path(""),
    path("submit/expense/",submit_expenses,name="submit_ex"),
    ]