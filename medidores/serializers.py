from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema

from .models import Medidores, Mediciones

def validate_nombre(value):
    if Medidores.objects.filter(nombre=value).exists():
        raise serializers.ValidationError("El nombre ya existe.")
    return value


class MedidoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medidores
        fields = [
            "nombre",
            "llave_id",
            "created",
        ]
        nombre = serializers.CharField(min_length=4, max_length=100, error_messages={"min_length": "Nombre debe tener al menos 4 caracteres"})


class MedicionesSerializer(serializers.ModelSerializer):
    consumo_reg = serializers.SerializerMethodField()
    class Meta:
        model = Mediciones
        fields = [
            "consumo_reg",
            "created",
            "medidor_id",
        ]

    def get_consumo_reg(self, obj):
        return f"{obj.consumo_reg}kw"
