from django.db import models

# Create your models here.
class teacher(models.Model):
    teachername = models.CharField(max_length=200)
    email = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.teachername
