from django.db import models

class Data(models.Model):
    first_name = models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField(default=1)