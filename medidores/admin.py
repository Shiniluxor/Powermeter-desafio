from django.contrib import admin
from django import forms

from . import models


class MedidoresAdminForm(forms.ModelForm):

    class Meta:
        model = models.Medidores
        fields = "__all__"


class MedidoresAdmin(admin.ModelAdmin):
    form = MedidoresAdminForm
    list_display = [
        "nombre",
        "llave_id",
        "created",
        "last_updated",
        "Id",
    ]
    readonly_fields = [
        "nombre",
        "llave_id",
        "created",
        "last_updated",
        "Id",
    ]


class MedicionesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Mediciones
        fields = "__all__"


class MedicionesAdmin(admin.ModelAdmin):
    form = MedicionesAdminForm
    list_display = [
        "id",
        "last_updated",
        "consumo_reg",
        "created",
    ]
    readonly_fields = [
        "id",
        "last_updated",
        "consumo_reg",
        "created",
    ]


admin.site.register(models.Medidores, MedidoresAdmin)
admin.site.register(models.Mediciones, MedicionesAdmin)
