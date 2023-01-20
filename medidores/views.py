from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Sum, Avg
from .models import Medidores, Mediciones
from . import forms

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import MedidoresSerializer, MedicionesSerializer

# MEDIDORES
#----------------------------------------------------------------
class MedidoresListView(generic.ListView):
    model = Medidores
    form_class = forms.MedidoresForm


class MedidoresListViewAPI(ListAPIView):
    queryset = Medidores.objects.all()
    serializer_class = MedidoresSerializer


class MedidoresCreateView(generic.CreateView):
    model = Medidores
    form_class = forms.MedidoresForm


class MedidoresCreateViewAPI(CreateAPIView):
    queryset = Medidores.objects.all()
    serializer_class = MedidoresSerializer


class MedidoresDetailView(generic.DetailView):
    model = Medidores
    form_class = forms.MedidoresForm
    pk_url_kwarg = "Id"


class MedidoresUpdateView(generic.UpdateView):
    model = Medidores
    form_class = forms.MedidoresForm
    pk_url_kwarg = "Id"


class MedidoresDeleteView(generic.DeleteView):
    model = Medidores
    success_url = reverse_lazy("Medidores_list")


class MedidorSearch(APIView):
    def get(self, request, format=None):
        key = request.GET.get('llave_id')
        medidor = Medidores.objects.get(llave_id=key)
        serializer = MedidoresSerializer(medidor)
        return Response(serializer.data, status=status.HTTP_200_OK)
#----------------------------------------------------------------
# MEDIDORES
#
# MEDICIONES
#----------------------------------------------------------------
class MedicionesListView(generic.ListView):
    model = Mediciones
    form_class = forms.MedicionesForm


class MedicionesListViewAPI(ListAPIView):
    queryset = Mediciones.objects.all()
    serializer_class = MedicionesSerializer


class MedicionesCreateView(generic.CreateView):
    model = Mediciones
    form_class = forms.MedicionesForm


class MedicionesCreateViewAPI(CreateAPIView):
    queryset = Mediciones.objects.all()
    serializer_class = MedicionesSerializer


class MedicionesDetailView(generic.DetailView):
    model = Mediciones
    form_class = forms.MedicionesForm
    pk_url_kwarg = "id"


class MedicionesUpdateView(generic.UpdateView):
    model = Mediciones
    form_class = forms.MedicionesForm
    pk_url_kwarg = "id"


class MedicionesDeleteView(generic.DeleteView):
    model = Mediciones
    success_url = reverse_lazy("Mediciones_list")
#----------------------------------------------------------------
# MEDICIONES


class ConsumoMaximoView(APIView):
    """
    Endpoint para obtener el consumo máximo de un medidor específico 
    """
    def get(self, request, format=None):
        """
        Obtiene el consumo máximo de un medidor específico atreves de su llave de identificación ("llave_id").
        """
        medidor = Medidores.objects.get(llave_id=request.GET.get('llave_id'))
        consumo_mas_alto = Mediciones.objects.filter(medidor_id=medidor).order_by("-consumo_reg").first()
        serializer = MedicionesSerializer(consumo_mas_alto)
        return Response(serializer.data)


class ConsumoMinimoView(APIView):
    """
    Endpoint para obtener el consumo máximo de un medidor específico 
    """
    def get(self, request, format=None):
        """
        Obtiene el consumo minimo de un medidor específico atreves de su llave de identificación ("llave_id").
        """
        medidor = Medidores.objects.get(llave_id=request.GET.get('llave_id'))
        consumo_mas_bajo = Mediciones.objects.filter(medidor_id=medidor).order_by("consumo_reg").first()
        serializer = MedicionesSerializer(consumo_mas_bajo)
        return Response(serializer.data)


class ConsumoTotalView(APIView):
    def get(self, request, format=None):
        medidor = Medidores.objects.get(llave_id=request.GET.get('llave_id'))
        total_consumo = Mediciones.objects.filter(medidor_id=medidor).aggregate(Sum('consumo_reg'))
        total_consumo = {'total_consumo': f"{total_consumo['consumo_reg__sum']}kw"}
        return Response(total_consumo)

class ConsumoPromedioView(APIView):
    def get(self, request, format=None):
        medidor = Medidores.objects.get(llave_id=request.GET.get('llave_id'))
        promedio_consumo = Mediciones.objects.filter(medidor_id=medidor).aggregate(Avg('consumo_reg'))
        promedio_consumo = {'promedio_consumo': f"{promedio_consumo['consumo_reg__avg']}kw"}
        return Response(promedio_consumo)
