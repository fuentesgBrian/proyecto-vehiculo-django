from django.db import models

# Create your models here.

MARCA_CHOICES = [
    ('Fiat','Fiat'),
    ('Chevrolet','Chevrolet'),
    ('Ford','Ford'),
    ('Toyota','Toyota')
]

CATEGORIA_CHOICES = [
    ('Particular','Particular'),
    ('Transporte','Transporte'),
    ('Carga','Carga')
]

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford', verbose_name='Marca')
    modelo = models.CharField(max_length=200, verbose_name='Modelo')
    serial_carro = models.CharField(max_length=50, verbose_name='Serial Carrocería')
    serial_motor = models.CharField(max_length=50, verbose_name='Serial Motor')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular', verbose_name='Categoría')
    precio = models.IntegerField(verbose_name='Precio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
    
    class Meta:
        ordering = ['marca']

    def __str__(self):
        return self.marca

    