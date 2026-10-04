from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import escape


from .models import (
    Certificado,
    AtendimentoChatbot,
    MensagemContato,

)


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'instituicao',
        'data_inicio',
        'data_termino',
        'carga_horaria',
    )

    ordering = (
        '-data_termino',
    )


@admin.register(AtendimentoChatbot)
class AtendimentoChatbotAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nome',
        'whatsapp',
        'email',
        'servico',
        'criado_em',
    )

    search_fields = (
        'nome',
        'whatsapp',
        'email',
        'servico',
    )

    list_filter = (
        'servico',
        'criado_em',
    )

    readonly_fields = (
        'criado_em',
        'atualizado_em',
        'conversa_formatada',
    )

    fieldsets = (
        (
            'Dados do Cliente',
            {
                'fields': (
                    'nome',
                    'whatsapp',
                    'email',
                    'servico',
                )
            }
        ),

        (
            'Conversa',
            {
                'fields': (
                    'conversa_formatada',
                )
            }
        ),

        (
            'Controle',
            {
                'fields': (
                    'criado_em',
                    'atualizado_em',
                )
            }
        ),
    )

    @admin.display(
        description='Conversa completa'
    )
    def conversa_formatada(self, obj):

        if not obj.mensagens:
            return 'Nenhuma mensagem registrada.'

        html = []

        for mensagem in obj.mensagens:

            tipo = mensagem.get(
                'tipo',
                ''
            )

            texto = mensagem.get(
                'mensagem',
                ''
            )

            # Protege o texto contra HTML
            texto = escape(texto)

            # Mensagem do cliente
            if tipo == 'cliente':

                html.append(
                    f'''
                    <div style="
                        background:#e8f5e9;
                        padding:12px;
                        margin-bottom:10px;
                        border-radius:8px;
                        border-left:4px solid #2e7d32;
                    ">
                        <strong>🟢 CLIENTE</strong>
                        <br><br>
                        {texto}
                    </div>
                    '''
                )

            # Mensagem do chatbot
            else:

                html.append(
                    f'''
                    <div style="
                        background:#eef3ff;
                        padding:12px;
                        margin-bottom:10px;
                        border-radius:8px;
                        border-left:4px solid #1e40af;
                    ">
                        <strong>🔵 CHAVIERWEBMÍDIA</strong>
                        <br><br>
                        {texto}
                    </div>
                    '''
                )

        return mark_safe(
            ''.join(html)
        )



@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'email',
        'whatsapp',
        'assunto',
        'respondido',
        'criado_em',
    )

    list_filter = (
        'respondido',
        'criado_em',
    )

    search_fields = (
        'nome',
        'email',
        'whatsapp',
        'assunto',
        'mensagem',
    )

    readonly_fields = (
        'criado_em',
    )

    ordering = (
        '-criado_em',
    )