from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)

    # Agregamos related_name para evitar conflictos con auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Cambiamos el related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Cambiamos el related_name
        blank=True
    )

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    profesor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='materias')
    creado_en = models.DateTimeField(auto_now_add=True)

class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'materia')

class Concepto(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

class Nota(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'concepto')

class Auditoria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=255)
    tabla_afectada = models.CharField(max_length=50)
    ip_cliente = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)