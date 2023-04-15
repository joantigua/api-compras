from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Entidades(models.Model):
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion

class Estados(models.Model):
    descripcion = models.CharField(max_length=50)
    entidad = models.ForeignKey(Entidades, on_delete = models.CASCADE)
    def __str__(self):
        return self.descripcion
    

class Departamentos(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.ForeignKey(Estados, on_delete = models.CASCADE)
    entidad = models.ForeignKey(Entidades, on_delete = models.CASCADE)

class Unidades_Medidas(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.ForeignKey(Estados, on_delete = models.CASCADE)
    entidad = models.ForeignKey(Entidades, on_delete = models.CASCADE)
    def __str__(self):
        return self.descripcion

class Proveedores(models.Model):
    nombre_comercial= models.CharField(max_length=50, verbose_name = "Nombre Comercial")
    cedula_rnc = models.CharField(max_length=11,  validators=[MinLengthValidator(11)],verbose_name = "Cedula o RNC")
    estado = models.ForeignKey(Estados, on_delete = models.CASCADE)
    entidad = models.ForeignKey(Entidades, on_delete = models.CASCADE)

class Articulos(models.Model):
    descripcion = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    existencia = models.IntegerField()
    estado = models.ForeignKey(Estados, on_delete = models.CASCADE)
    entidad = models.ForeignKey(Entidades, on_delete = models.CASCADE)
    unidad_medida = models.ForeignKey(Unidades_Medidas, on_delete = models.CASCADE, default = "")
    def __str__(self):
        return self.descripcion

class Orden_Compra(models.Model):
    fecha = models.DateTimeField()
    articulo = models.ForeignKey(Articulos, on_delete = models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    unidad_medida = models.ForeignKey(Unidades_Medidas, on_delete = models.CASCADE, default = "")
    costo_unitario = models.IntegerField(default = 0)
    estado = models.ForeignKey(Estados, on_delete = models.CASCADE)
    entidad = models.ForeignKey(Entidades, on_delete = models.CASCADE)
    id_asiento = models.CharField(default="null", max_length=4)
    
    def total_orden(self):
        total_orden = self.cantidad * self.costo_unitario
        return total_orden
    def __str__(self):
        name = str(self.id)
        return name

class Asiento(models.Model):
    TIPO_TRANSACCIONES = (
        ('Debito', 'Debito'),
        ('Credito', 'Credito'),
    )
    periodo_asiento_desde = models.DateField()
    periodo_asiento_hasta = models.DateField()
    transaccion = models.ManyToManyField(Orden_Compra)
    id_cuenta_db = models.CharField(max_length=10)
    descripcion_db = models.CharField(max_length= 40)
    id_cuenta_cr = models.CharField(max_length=10)
    descripcion_cr = models.CharField(max_length= 40)
    monto_db = models.IntegerField()
    monto_cr = models.IntegerField()