from django import forms
from django.forms import ModelForm
from .models import *

class EntidadesForm(ModelForm):
    class Meta:
      model = Entidades
      fields = '__all__'

class EstadosForm(ModelForm):
    class Meta:
      model = Estados
      fields = '__all__'

class DepartamentosForm(ModelForm):
    class Meta:
      model = Departamentos
      fields = '__all__'   

class Unidades_MedidasForm(ModelForm):
    class Meta:
      model = Unidades_Medidas
      fields = '__all__'   

class ProveedoresForm(ModelForm):
    class Meta:
      model = Proveedores
      fields = '__all__'   

class ArticulosForm(ModelForm):
    class Meta:
      model = Articulos
      fields = '__all__'   

class Orden_CompraForm(ModelForm):
    class Meta:
      model = Orden_Compra
      fields = '__all__'   

class AsientoForm(ModelForm):
    class Meta:
      model = Asiento
      fields = '__all__'   