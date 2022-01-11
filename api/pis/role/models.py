from django.db import models

class Rola(models.Model):
    rola = models.CharField(max_length=15)
    