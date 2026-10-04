
from django.shortcuts import render

from django.http import JsonResponse

from django.views.decorators.http import require_POST

import json
import re

from .models import (
    Certificado,
    AtendimentoChatbot,
)

from .forms import MensagemContatoForm


# ==========================================
# HOME
# ==========================================

def home(request):

    return render(
        request,
        'home.html'
    )


# ==========================================
# SOBRE
# ==========================================

def sobre(request):

    return render(
        request,
        'sobre.html'
    )


# ==========================================
# CONTATOS
# ==========================================

def contatos(request):

    if request.method == 'POST':

        formulario = MensagemContatoForm(
            request.POST
        )

        if formulario.is_valid():

            formulario.save()

            return render(
                request,
                'contatos.html',
                {
                    'formulario': MensagemContatoForm(),
                    'sucesso': True,
                }
            )

    else:

        formulario = MensagemContatoForm()

    return render(
        request,
        'contatos.html',
        {
            'formulario': formulario,
        }
    )


# ==========================================
# QUALIFICAÇÕES
# ==========================================

def qualificacoes(request):

    certificados = Certificado.objects.all()

    return render(
        request,
        'qualificacoes.html',
        {
            'certificados': certificados
        }
    )


# ==========================================
# CHATBOT
# ==========================================

@require_POST
def chatbot_mensagem(request):

    try:

        dados = json.loads(
            request.body
        )

        mensagem = dados.get(
            'mensagem',
            ''
        ).strip()

        atendimento_id = dados.get(
            'atendimento_id'
        )

        etapa = dados.get(
            'etapa',
            ''
        )

        # ==================================
        # VALIDA MENSAGEM VAZIA
        # ==================================

        if not mensagem:

            return JsonResponse(
                {
                    'sucesso': False,
                    'erro': (
                        '⚠️ Por favor, '
                        'digite uma mensagem.'
                    )
                },
                status=400
            )

        # ==================================
        # LOCALIZA ATENDIMENTO
        # ==================================

        if atendimento_id:

            try:

                atendimento = (
                    AtendimentoChatbot.objects.get(
                        id=atendimento_id
                    )
                )

            except AtendimentoChatbot.DoesNotExist:

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ Atendimento '
                            'não encontrado.'
                        )
                    },
                    status=404
                )

        else:

            atendimento = (
                AtendimentoChatbot.objects.create()
            )

        # ==================================
        # NOME
        # ==================================

        if etapa == 'nome':

            nome = ' '.join(
                mensagem.split()
            )

            if len(nome) < 2:

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ Informe seu nome '
                            'corretamente.'
                            '<br><br>'
                            'Digite pelo menos '
                            '<strong>2 caracteres</strong>.'
                        )
                    },
                    status=400
                )

            if re.search(
                r'\d',
                nome
            ):

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ O nome não deve '
                            'conter números.'
                            '<br><br>'
                            'Digite seu nome corretamente.'
                        )
                    },
                    status=400
                )

            atendimento.nome = nome

            resposta = (
                'Prazer em conhecer você! 😊'
                '<br><br>'
                'Agora informe seu '
                '<strong>WhatsApp</strong>.'
                '<br><br>'
                'Exemplo: '
                '<strong>(21) 99999-9999</strong>'
            )

        # ==================================
        # WHATSAPP
        # ==================================

        elif etapa == 'whatsapp':

            whatsapp = re.sub(
                r'\D',
                '',
                mensagem
            )

            if len(whatsapp) not in (
                10,
                11
            ):

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ WhatsApp inválido.'
                            '<br><br>'
                            'Informe um número com DDD.'
                            '<br><br>'
                            'Exemplo: '
                            '<strong>(21) 99999-9999</strong>'
                        )
                    },
                    status=400
                )

            if len(set(whatsapp)) == 1:

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ Número de WhatsApp inválido.'
                            '<br><br>'
                            'Informe um número válido.'
                        )
                    },
                    status=400
                )

            atendimento.whatsapp = whatsapp

            resposta = (
                'Perfeito! 📱'
                '<br><br>'
                'Agora informe seu '
                '<strong>e-mail</strong>.'
                '<br><br>'
                'Exemplo: '
                '<strong>nome@email.com</strong>'
            )

        # ==================================
        # E-MAIL
        # ==================================

        elif etapa == 'email':

            email = mensagem.lower()

            padrao_email = (
                r'^[a-zA-Z0-9._%+-]+'
                r'@[a-zA-Z0-9.-]+'
                r'\.[a-zA-Z]{2,}$'
            )

            if not re.match(
                padrao_email,
                email
            ):

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ E-mail inválido.'
                            '<br><br>'
                            'Digite um e-mail válido.'
                            '<br><br>'
                            'Exemplo: '
                            '<strong>nome@email.com</strong>'
                        )
                    },
                    status=400
                )

            if len(email) > 254:

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ E-mail muito longo.'
                            '<br><br>'
                            'Digite um e-mail válido.'
                        )
                    },
                    status=400
                )

            atendimento.email = email

            resposta = (
                'Obrigado! 📧'
                '<br><br>'
                'Agora escolha qual '
                '<strong>serviço</strong> '
                'você procura.'
                '<br><br>'

                '<strong>1️⃣</strong> Solicitar orçamento'
                '<br>'

                '<strong>2️⃣</strong> Conhecer nossos serviços'
                '<br>'

                '<strong>3️⃣</strong> Criar um site'
                '<br>'

                '<strong>4️⃣</strong> Criar uma Landing Page'
                '<br>'

                '<strong>5️⃣</strong> Criar um Sistema Web'
                '<br>'

                '<strong>6️⃣</strong> Outro projeto'
            )

        # ==================================
        # SERVIÇO
        # ==================================

        elif etapa == 'servico':

            servicos = {

                '1': 'Solicitar orçamento',

                '2': 'Conhecer nossos serviços',

                '3': 'Criar um site',

                '4': 'Criar uma Landing Page',

                '5': 'Criar um Sistema Web',

                '6': 'Outro projeto',
            }

            if mensagem not in servicos:

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ Opção inválida.'
                            '<br><br>'
                            'Escolha uma opção de '
                            '<strong>1 a 6</strong>.'
                        )
                    },
                    status=400
                )

            atendimento.servico = (
                servicos[mensagem]
            )

            resposta = (
                'Excelente escolha! 🚀'
                '<br><br>'
                f'<strong>{servicos[mensagem]}</strong>'
                '<br><br>'
                'Agora conte um pouco mais sobre '
                'o <strong>projeto</strong> que você '
                'deseja realizar.'
                '<br><br>'
                'Digite pelo menos '
                '<strong>10 caracteres</strong>.'
            )

        # ==================================
        # MENSAGEM / PROJETO
        # ==================================

        elif etapa == 'mensagem':

            projeto = mensagem.strip()

            if len(projeto) < 10:

                return JsonResponse(
                    {
                        'sucesso': False,
                        'erro': (
                            '⚠️ Sua mensagem está muito curta.'
                            '<br><br>'
                            'Conte um pouco mais sobre '
                            'o projeto.'
                            '<br><br>'
                            'Digite pelo menos '
                            '<strong>10 caracteres</strong>.'
                        )
                    },
                    status=400
                )

            resposta = (
                'Obrigado pelas informações! 😊'
                '<br><br>'
                'Seu atendimento foi registrado '
                '<strong>com sucesso</strong>.'
                '<br><br>'
                'Nossa equipe poderá analisar '
                'seu projeto e entrar em contato.'
            )

        # ==================================
        # ETAPA DESCONHECIDA
        # ==================================

        else:

            resposta = (
                'Obrigado pela sua mensagem! 😊'
            )

        # ==================================
        # SALVA MENSAGEM DO CLIENTE
        # ==================================

        atendimento.mensagens.append(
            {
                'tipo': 'cliente',
                'mensagem': mensagem
            }
        )

        # ==================================
        # SALVA RESPOSTA DO BOT
        # ==================================

        atendimento.mensagens.append(
            {
                'tipo': 'bot',
                'mensagem': resposta
            }
        )

        # ==================================
        # SALVA ATENDIMENTO
        # ==================================

        atendimento.save()

        # ==================================
        # RETORNO PARA JAVASCRIPT
        # ==================================

        return JsonResponse(
            {
                'sucesso': True,
                'atendimento_id': atendimento.id,
                'resposta': resposta
            }
        )

    # ======================================
    # ERRO JSON
    # ======================================

    except json.JSONDecodeError:

        return JsonResponse(
            {
                'sucesso': False,
                'erro': (
                    '⚠️ Dados enviados '
                    'em formato inválido.'
                )
            },
            status=400
        )

    # ======================================
    # ERRO GERAL
    # ======================================

    except Exception as erro:

        return JsonResponse(
            {
                'sucesso': False,
                'erro': str(erro)
            },
            status=500
        )

