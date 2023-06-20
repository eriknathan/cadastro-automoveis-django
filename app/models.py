from django.db import models


# Create your models here.
class Vinhos(models.Model):
    acidez_fixa = models.DecimalField(max_digits=10, decimal_places=6)
    acidez_volátil = models.DecimalField(max_digits=10, decimal_places=6)
    acido_cítrico = models.DecimalField(max_digits=10, decimal_places=6)
    acucar_residual = models.DecimalField(max_digits=10, decimal_places=6)
    cloretos = models.DecimalField(max_digits=10, decimal_places=6)
    dióxido_de_enxofre_livre = models.DecimalField(max_digits=10, decimal_places=6)
    dióxido_de_enxofre_total = models.DecimalField(max_digits=10, decimal_places=6)
    densidade = models.DecimalField(max_digits=10, decimal_places=6)
    pH = models.DecimalField(max_digits=10, decimal_places=6)
    sulfatos = models.DecimalField(max_digits=10, decimal_places=6)
    álcool = models.DecimalField(max_digits=10, decimal_places=6)