from django.db import models
from django.db.models.base import Model

class Cjenovnik(models.Model):
    date_created=models.DateField(auto_now_add=True)
    kategorija1_cijena=models.DecimalField(max_digits=4, decimal_places=2)
    kategorija2_cijena=models.DecimalField(max_digits=4, decimal_places=2)
    kategorija3_cijena=models.DecimalField(max_digits=4, decimal_places=2)
    kategorija1_granica=models.IntegerField()
    kategorija2_granica=models.IntegerField()
    
