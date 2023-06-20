from django.forms import ModelForm
from app.models import Vinhos


# Create the form class.
class VinhosForm(ModelForm):
    class Meta:
        model = Vinhos
        fields = ["acidez_fixa", "acidez_volátil", "acido_cítrico", "acucar_residual", "cloretos", "dióxido_de_enxofre_livre", "dióxido_de_enxofre_total", "densidade", "pH", "sulfatos", "álcool"]
