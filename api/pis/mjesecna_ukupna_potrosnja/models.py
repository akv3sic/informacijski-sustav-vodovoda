from django.db import models

class MjesecnaUkupnaPotrosnja(models.Model):
    mjesec = models.CharField(max_length=15)
    volumen= models.DecimalField(decimal_places=3, max_digits=15)

