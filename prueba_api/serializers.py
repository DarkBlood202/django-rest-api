from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Reporte, Pregunta


class ReporteSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Reporte
        fields = '__all__'


class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    autor = serializers.ReadOnlyField(source='autor.username')

    class Meta:
        model = Pregunta
        fields = '__all__'

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    reportes = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='reporte-detalle',
        read_only=True
    )

    preguntas = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='pregunta-detalle',
        read_only=True
    )

    # reportes = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Reporte.objects.all()
    # )

    # preguntas = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Pregunta.objects.all()
    # )

    class Meta:
        model = User
        fields = ['id', 'username', 'reportes', 'preguntas']