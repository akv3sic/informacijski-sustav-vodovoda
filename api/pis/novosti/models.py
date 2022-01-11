from django.db import models
from django.db.models.deletion import CASCADE

from korisnici.models import User

class Novost(models.Model):
    date_created=models.DateField(auto_now_add=True)
    naslov= models.CharField(max_length=100, null=False)
    tekst=models.TextField()
    korisnik=models.ForeignKey(User, on_delete=CASCADE)
    