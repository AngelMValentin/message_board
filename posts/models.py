from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DataTimeField(auto_now_add=True)