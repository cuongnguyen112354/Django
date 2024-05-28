from django.db import models

class Student(models.Model):
   maso = models.CharField(max_length=10)
   ho = models.CharField(max_length=30)
   ten = models.CharField(max_length=10)
   qt1 = models.FloatField(default=0)
   qt2 = models.FloatField(default=0)
   mid = models.FloatField(default=0)
   final = models.FloatField(default=0)