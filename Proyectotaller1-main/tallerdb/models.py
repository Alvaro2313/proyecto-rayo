from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=15)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)      