from django.db import models
from django.db.models.deletion import CASCADE


from prikljucci.models import Prikljucak

class Dokumenti(models.Model):
    zahtjev=models.CharField(max_length=150, null=False)
    zk_izvadak=models.CharField(max_length=150, null=False)
    katastarski_plan=models.CharField(max_length=150, null=False)
    prikljucak=models.ForeignKey(Prikljucak, on_delete=CASCADE)

