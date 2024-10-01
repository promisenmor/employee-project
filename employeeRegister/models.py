from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)


class Employee(models.Model):
    Fullname = models.CharField(max_length=250)
    Emp_code = models.CharField(max_length=5)
    position = models.ForeignKey(Position, on_delete= models.CASCADE)
    mobile = models.CharField(max_length=15)
    Address =  models.CharField(max_length=250)
    EMail = models.EmailField


