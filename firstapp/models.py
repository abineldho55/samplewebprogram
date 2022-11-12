from django.db import models

class students(models.Model):
     studentname=models.CharField(max_length=100)
     email=models.CharField(max_length=200,null=True)
     rollno=models.CharField(max_length=200)
     course=models.CharField(max_length=200)
     age=models.IntegerField()
     address=models.TextField()

     def __str__(self):
         return self.studentname



# Create your models here.
