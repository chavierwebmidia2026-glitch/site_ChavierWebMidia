from django.db import models


class Certificado(models.Model):

    nome = models.CharField(max_length=200)

    instituicao = models.CharField(max_length=150)

    data_inicio = models.DateField()

    data_termino = models.DateField()

    carga_horaria = models.PositiveIntegerField()

    descricao = models.TextField()

    imagem = models.ImageField(
        upload_to='certificados/',
        blank=True,
        null=True
    )

    certificado = models.FileField(
        upload_to='certificados/',
        blank=True,
        null=True,
        max_length=255
    )

    def __str__(self):
        return self.nome


class AtendimentoChatbot(models.Model):

    nome = models.CharField(
        max_length=150,
        blank=True
    )

    whatsapp = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    servico = models.CharField(
        max_length=150,
        blank=True
    )

    mensagens = models.JSONField(
        default=list,
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        if self.nome:
            return self.nome

        return f"Atendimento #{self.id}"



class MensagemContato(models.Model):

    nome = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    whatsapp = models.CharField(
        max_length=30,
        blank=True
    )

    assunto = models.CharField(
        max_length=200
    )

    mensagem = models.TextField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    respondido = models.BooleanField(
        default=False
    )

    def __str__(self):

        return f"{self.nome} - {self.assunto}"

