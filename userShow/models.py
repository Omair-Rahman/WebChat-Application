from django.db import models

# Create your models here.
class displayUsername(models.Model):
    userName = models.CharField(max_length=100)
