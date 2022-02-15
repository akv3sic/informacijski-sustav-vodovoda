from django.db import models
from django.db.models.deletion import CASCADE
from cjenovnik.models import Cjenovnik

from korisnici.models import User
from prikljucci.models import Prikljucak

class Racun(models.Model):
    date_created=models.DateField(auto_now=True)
    brojilo=models.DecimalField(decimal_places=3, max_digits=11)
    potrosnja=models.DecimalField(decimal_places=3, max_digits=11)
    iznos=models.DecimalField(decimal_places=2, max_digits=6)
    dug=models.DecimalField(decimal_places=2, max_digits=6)
    popisivac=models.ForeignKey(User, on_delete=CASCADE)
    prikljucak=models.ForeignKey(Prikljucak, on_delete=CASCADE)
    cjenovnik=models.ForeignKey(Cjenovnik, on_delete=CASCADE)
    on_hold=models.BooleanField(default=True)
    placeno=models.BooleanField(default=False)
    datum_dospijeca=models.DateField(default=None, blank=True, null=True)
    datum_placanja=models.DateField(default=None, blank=True, null=True)
    mjesec=models.CharField(max_length=8, default=None)

    @property
    def ukupno(self):
        return (self.iznos+self.dug)
    
    @property
    def prethodno_stanje(self):
        return (self.brojilo - self.potrosnja)
        
    
