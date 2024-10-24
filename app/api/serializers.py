from rest_framework import serializers
from .models import Usuario, Rol, Materia, Inscripcion, Concepto, Nota

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'matricula', 'rol']

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ['id', 'nombre', 'codigo', 'descripcion', 'profesor']

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id', 'usuario', 'concepto', 'calificacion', 'fecha']
