from django.contrib import admin
from .models import Income,Expense,Token
# Register your models here.

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Token)
