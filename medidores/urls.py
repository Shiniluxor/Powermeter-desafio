from django.urls import path, include
from rest_framework import routers


from . import api
from . import views


router = routers.DefaultRouter()
router.register("Medidores", api.MedidoresViewSet)
router.register("Mediciones", api.MedicionesViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Medidores/", views.MedidoresListView.as_view(), name="Medidores_list"),
    path("Medidores_lista/", views.MedidoresListViewAPI.as_view(), name="Medidores_lista"),
    path("Medidores/create/", views.MedidoresCreateView.as_view(), name="Medidores_create"),
    path("Medidores/new/", views.MedidoresCreateViewAPI.as_view(), name="medidor_new"),
    path("Medidores/detail/<int:Id>/", views.MedidoresDetailView.as_view(), name="Medidores_detail"),
    path("Medidores/search/", views.MedidorSearch.as_view(), name="Medidores_search"),
    path("Medidores/update/<int:Id>/", views.MedidoresUpdateView.as_view(), name="Medidores_update"),
    path("Medidores/delete/<int:pk>/", views.MedidoresDeleteView.as_view(), name="Medidores_delete"),
    path("Mediciones/", views.MedicionesListView.as_view(), name="Mediciones_list"),
    path("Mediciones_lista/", views.MedicionesListViewAPI.as_view(), name="Mediciones_lista"),
    path("Mediciones/new/", views.MedicionesCreateViewAPI.as_view(), name="medicion_new"),
    path("Mediciones/create/", views.MedicionesCreateView.as_view(), name="Mediciones_create"),
    path("Mediciones/detail/<int:id>/", views.MedicionesDetailView.as_view(), name="Mediciones_detail"),
    path("Mediciones/update/<int:id>/", views.MedicionesUpdateView.as_view(), name="Mediciones_update"),
    path("Mediciones/delete/<int:pk>/", views.MedicionesDeleteView.as_view(), name="Mediciones_delete"),
    path('Mediciones/consumo_maximo/', views.ConsumoMaximoView.as_view(), name='medicion_maxima'),
    path('Mediciones/consumo_minimo/', views.ConsumoMinimoView.as_view(), name='medicion_minima'),
    path('Mediciones/consumo_total/', views.ConsumoTotalView.as_view(), name='consumo_total'),
    path('Mediciones/consumo_promedio/', views.ConsumoPromedioView.as_view(), name='consumo_promedio'),
)
