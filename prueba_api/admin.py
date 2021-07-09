from django.contrib import admin
from .models import Reporte, Pregunta

# Register your models here.
@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    ordering = ['fecha']
    list_display_links = ('titulo','usuario')
    list_display = ('titulo','usuario')

    list_filter = ('titulo', 'fecha', 'usuario')
    search_fields = ['titulo', 'usuario']


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    ordering = ['fecha']
    list_display_links = ('titulo','autor')
    list_display = ('titulo','autor')

    list_filter = ('titulo', 'fecha', 'autor')
    search_fields = ['titulo', 'autor']