
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .filters import *
from django.core import serializers
from django.forms.models import model_to_dict


import datetime

def home(request):
    return render(request, 'sistema_compras/home_page.html')

def entidades(request):
  entidades = Entidades.objects.all()
  return render(request, 'sistema_compras/entidades.html', {'entidades' : entidades})

def createEntidades(request):
  form = EntidadesForm()
  context = {'form' : form}
  if request.method == 'POST':
     form = EntidadesForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/entidades')
  return render(request, 'sistema_compras/entidades_form.html', context)
  
def updateEntidades(request, id):
  entidades = Entidades.objects.get(pk = id)
  form = EntidadesForm(request.POST or None, instance = entidades)
  if form.is_valid():
      form.save()
      return redirect('/entidades')
  context = { 
    'form':form,
    'entidades':entidades,
  }
  return render(request, 'sistema_compras/entidades_form_update.html', context)   
        
def deleteEntidades(request, id):
  entidades = Entidades.objects.get(pk = id)
  entidades.delete()
  return redirect('/entidades')


def estados(request):
  estados = Estados.objects.all()
  return render(request, 'sistema_compras/estados.html', {'estados' : estados})

def createEstados(request):
  form = EstadosForm()
  context = {'form' : form}
  if request.method == 'POST':
     form = EstadosForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/estados')
  return render(request, 'sistema_compras/estados_form.html', context)
  
def updateEstados(request, id):
  estados = Estados.objects.get(pk = id)
  form = EstadosForm(request.POST or None, instance = estados)
  if form.is_valid():
      form.save()
      return redirect('/estados')
  context = { 
    'form':form,
    'estados':estados,
  }
  return render(request, 'sistema_compras/estados_form_update.html', context)   
        
def deleteEstados(request, id):
  
  estados = Estados.objects.get(pk = id)
  estados.delete()
  return redirect('/estados')

def departamentos(request):
  departamentos = Departamentos.objects.all()
  return render(request, 'sistema_compras/departamentos.html', {'departamentos' : departamentos})

def createDepartamentos(request):
  form = DepartamentosForm()
  context = {'form' : form}
  if request.method == 'POST':
     form = DepartamentosForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/departamentos')
  return render(request, 'sistema_compras/departamentos_form.html', context)
  
def updateDepartamentos(request, id):
  departamentos = Departamentos.objects.get(pk = id)
  form = DepartamentosForm(request.POST or None, instance = departamentos)
  if form.is_valid():
      form.save()
      return redirect('/departamentos')
  context = { 
    'form':form,
    'departamentos':departamentos,
  }
  return render(request, 'sistema_compras/departamentos_form_update.html', context)   
        
def deleteDepartamentos(request, id):
  departamentos = Departamentos.objects.get(pk = id)
  departamentos.delete()
  return redirect('/departamentos')

def unidadesMedidas(request):
  unidadesMedidas = Unidades_Medidas.objects.all()
  return render(request, 'sistema_compras/unidadesMedidas.html', {'unidadesMedidas' : unidadesMedidas})

def createUnidadesMedidas(request):
  form = Unidades_MedidasForm()
  context = {'form' : form}
  if request.method == 'POST':
     form = Unidades_MedidasForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/unidadesMedidas')
  return render(request, 'sistema_compras/unidadesMedidas_form.html', context)
  
def updateUnidadesMedidas(request, id):
  unidadesMedidas = Unidades_Medidas.objects.get(pk = id)
  form = Unidades_MedidasForm(request.POST or None, instance = unidadesMedidas)
  if form.is_valid():
      form.save()
      return redirect('/unidadesMedidas')
  context = { 
    'form':form,
    'unidadesMedidas':unidadesMedidas,
  }
  return render(request, 'sistema_compras/unidadesMedidas_form_update.html', context)   
        
def deleteUnidadesMedidas(request, id):
  unidadesMedidas = Unidades_Medidas.objects.get(pk = id)
  unidadesMedidas.delete()
  return redirect('/unidadesMedidas')

def proveedores(request):
  proveedores = Proveedores.objects.all()
  return render(request, 'sistema_compras/proveedores.html', {'proveedores' : proveedores})

def createProveedores(request):
  form = ProveedoresForm()
  context = {'form' : form}
  if request.method == 'POST':
     form = ProveedoresForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/proveedores')
  return render(request, 'sistema_compras/proveedores_form.html', context)
  
def updateProveedores(request, id):
  proveedores = Proveedores.objects.get(pk = id)
  form = ProveedoresForm(request.POST or None, instance = proveedores)
  if form.is_valid():
      form.save()
      return redirect('/proveedores')
  context = { 
    'form':form,
    'proveedores':proveedores,
  }
  return render(request, 'sistema_compras/proveedores_form_update.html', context)   
        
def deleteProveedores(request, id):
  
  proveedores = Proveedores.objects.get(pk = id)
  proveedores.delete()
  return redirect('/proveedores')

def articulos(request):
  articulos = Articulos.objects.all()
  return render(request, 'sistema_compras/articulos.html', {'articulos' : articulos})

def createArticulos(request):
  form = ArticulosForm()
  context = {'form' : form}
  if request.method == 'POST':
     form = ArticulosForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/articulos')
  return render(request, 'sistema_compras/articulos_form.html', context)
  
def updateArticulos(request, id):
  articulos = Articulos.objects.get(pk = id)
  form = ArticulosForm(request.POST or None, instance = articulos)
  if form.is_valid():
      form.save()
      return redirect('/articulos')
  context = { 
    'form':form,
    'articulos':articulos,
  }
  return render(request, 'sistema_compras/articulos_form_update.html', context)   
        
def deleteArticulos(request, id):
  
  articulos = Articulos.objects.get(pk = id)
  articulos.delete()
  return redirect('/articulos')



def ordenCompra(request):
  ordenCompra = Orden_Compra.objects.all()
  myFilter = OrderFilter(request.GET, queryset = ordenCompra)
  ordenCompra = myFilter.qs

  total_sum = 0
  for item in ordenCompra:
      total_sum = total_sum + item.total_orden()
  context = {'ordenCompra' : ordenCompra, 'myFilter' : myFilter, 'total_sum' : total_sum}
  return render(request, 'sistema_compras/ordenCompra.html', context)
  

def createOrdenCompra(request):
  form = Orden_CompraForm()
  context = {'form' : form}
  if request.method == 'POST':
     form = Orden_CompraForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/ordenCompra')
  return render(request, 'sistema_compras/ordenCompra_form.html', context)
  
def updateOrdenCompra(request, id):
  ordenCompra = Orden_Compra.objects.get(pk = id)
  form = Orden_CompraForm(request.POST or None, instance = ordenCompra)
  if form.is_valid():
      form.save()
      return redirect('/ordenCompra')
  context = { 
    'form':form,
    'ordenCompra':ordenCompra,
  }
  return render(request, 'sistema_compras/ordenCompra_form_update.html', context)   
        
def deleteOrdenCompra(request, id):
  
  ordenCompra = Orden_Compra.objects.get(pk = id)
  ordenCompra.delete()
  return redirect('/ordenCompra')

def asiento(request):
  asiento = Asiento.objects.all()
  return render(request, 'sistema_compras/asiento.html', {'asiento' : asiento})

def createAsientoJson(request, id ):
   asiento = Asiento.objects.filter(id = id)
   res = serializers.serialize("json", asiento)
   with open('data.json', 'w') as f:
    f.write(res)
   return redirect('/asiento')

def createAsiento(request):
  form = AsientoForm()
  context = {'form' : form}
  if request.method == 'POST':
     form = AsientoForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/asiento')
  return render(request, 'sistema_compras/asiento_form.html', context)
  
def updateAsiento(request, id):
  asiento = Asiento.objects.get(pk = id)
  form = AsientoForm(request.POST or None, instance = asiento)
  if form.is_valid():
      form.save()
      return redirect('/asiento')
  context = { 
    'form':form,
    'asiento':asiento,
  }
  return render(request, 'sistema_compras/asiento_form_update.html', context)   
        
def deleteAsiento(request, id):
  asiento = Asiento.objects.get(pk = id)
  asiento.delete()
  return redirect('/asiento')

