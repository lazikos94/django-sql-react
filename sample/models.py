# Create your models here.
from django.db import models

class Sample(models.Model):
    title = models.CharField(max_length=200, default='something')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title