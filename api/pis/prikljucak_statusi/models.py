from django.db import models

class StatusPrikljucka(models.Model):
    status=models.CharField(max_length=50, null=False)
    