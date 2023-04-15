import django_filters
from django_filters import DateFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name= "fecha", lookup_expr="gte")
    end_date = DateFilter(field_name= "fecha", lookup_expr="lte")
    class Meta:
        model = Orden_Compra
        fields = '__all__'
        exclude = ['fecha', 'articulo', 'cantidad', 'unidad_medida', 'total_orden', 'estado', 'costo_unitario', 'entidad', 'id_asiento']
        