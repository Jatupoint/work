from django.db import models

# Create your models here.
class Members(models.Model):
    name =models.CharField(max_length=200)
    desc =models.TextField()

class Class(models.Model):
    code = models.CharField(max_length=100)
    username = models.CharField(max_length= 100)

class Student(models.Model):
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    classcode = models.CharField(max_length=50)
    classroom = models.CharField(max_length=50)

class Teacher(models.Model):
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    classcode = models.CharField(max_length=50)
    classroom = models.CharField(max_length=50)