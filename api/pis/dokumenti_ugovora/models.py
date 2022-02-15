from django.db import models
from django.db.models.deletion import CASCADE


from prikljucci.models import Prikljucak

class Dokumenti(models.Model):
    zahtjev=models.FileField(blank=False, null=False)
    zk_izvadak=models.FileField(blank=False, null=False)
    katastarski_plan=models.FileField(blank=False, null=False)
    prikljucak=models.ForeignKey(Prikljucak, on_delete=CASCADE)
    

