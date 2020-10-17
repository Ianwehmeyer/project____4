from django.db import models

# Create your models here.
class Account( models.Model):
    balance = models. DecimalField(max_digits=20, decimal_places=2);
    #NOTE FOR SELF - balance will act as the amount of cash funds in User's account


class Things( models.Model): #figure out what we're supposed to do with this
    amount = models.DecimalField(max_digits=20, decimal_places=2); #values that should be decimal
    name = models.CharField( max_length=30)