from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)


class Employee(models.Model):
    Fullname = models.CharField(max_length=250)
    Emp_code = models.IntegerField
    position = models.ForeignKey(Position, on_delete= models.CASCADE)
    mobile = models.IntegerField
    Address =  models.CharField(max_length=250)
    EMail = models.EmailField


