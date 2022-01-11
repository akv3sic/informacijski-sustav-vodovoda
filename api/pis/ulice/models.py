from django.db import models
from django.db.models.deletion import CASCADE

from mjesta.models import Mjesto

class Ulica(models.Model):
    ulica=models.CharField(max_length=50)
    mjesto=models.ForeignKey(Mjesto, on_delete=CASCADE)
    