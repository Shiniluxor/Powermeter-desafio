from rest_framework import viewsets, permissions

from . import serializers
from . import models


class MedidoresViewSet(viewsets.ModelViewSet):
    """ViewSet for the Medidores class"""

    queryset = models.Medidores.objects.all()
    serializer_class = serializers.MedidoresSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedicionesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Mediciones class"""

    queryset = models.Mediciones.objects.all()
    serializer_class = serializers.MedicionesSerializer
    permission_classes = [permissions.IsAuthenticated]
