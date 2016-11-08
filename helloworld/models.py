from django.db import models

class Messages(models.Model):
    msg = models.CharField(max_length=120)
