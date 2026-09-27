from django.shortcuts import render
from .models import Certificado



def home(request):
    return render (request, 'home.html')



def sobre(request):
    return render (request, 'sobre.html')


def contatos(request):
    return render (request, 'contatos.html')


def qualificacoes(request):

    certificados = Certificado.objects.all()

    return render(
        request,
        'qualificacoes.html',
        {
            'certificados': certificados
        }
    )