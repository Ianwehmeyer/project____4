from django.db import models

# Create your models here.
class Account( models,Model):
    balance = models. IntegerField();
    #NOTE FOR SELF - balance will act as the amount of cash funds in User's account