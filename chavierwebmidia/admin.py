
from django.contrib import admin
from .models import Certificado


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'instituicao',
        'data_inicio',
        'data_termino',
        'carga_horaria',
    )

    ordering = ('-data_termino',)