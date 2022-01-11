from django.db import models
from django.db.models.deletion import CASCADE
from korisnici.models import User

from prikljucci.models import Prikljucak
from tiket_statusi.models import StatusTiketa

class Tiket(models.Model):
    naslov=models.CharField(max_length=50, null=False)
    pitanje=models.TextField()
    odgovor=models.TextField(default=None)
    prikljucak=models.ForeignKey(Prikljucak, on_delete=CASCADE)
    racunovodja=models.ForeignKey(User, on_delete=CASCADE)
    status=models.ForeignKey(StatusTiketa, on_delete=CASCADE)