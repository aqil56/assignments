from django.db import models

# Create your models here.
class Talk(models.Model):
    properties_ID= models.IntegerField(default=0)
    Name= models.CharField(max_length=30)
    Speaker= models.CharField(max_length=30)
    Venue= models.TextField(max_length=300)
    Duration= models.CharField(max_length=30)