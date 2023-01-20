from django import forms
from medidores.models import Medidores
from . import models


class MedidoresForm(forms.ModelForm):
    class Meta:
        model = models.Medidores
        fields = [
            "nombre",
            "llave_id",
        ]


class MedicionesForm(forms.ModelForm):
    class Meta:
        model = models.Mediciones
        fields = [
            "consumo_reg",
            "medidor_id",
        ]

    def __init__(self, *args, **kwargs):
        super(MedicionesForm, self).__init__(*args, **kwargs)
        self.fields["medidor_id"].queryset = Medidores.objects.all()

