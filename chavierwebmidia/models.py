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
