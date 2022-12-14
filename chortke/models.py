from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Token(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.TextField(max_length=8)

    def __str__(self) -> str:
        return "{} - ToKeN".format(self.user)

#####
    
class Expense(models.Model):
    text=models.CharField(max_length=250)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
#####

class Income(models.Model):
    text=models.CharField(max_length=250)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
    
