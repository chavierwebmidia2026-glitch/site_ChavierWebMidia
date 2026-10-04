
from django import forms
import re

from .models import MensagemContato


class MensagemContatoForm(forms.ModelForm):

    class Meta:

        model = MensagemContato

        fields = (
            'nome',
            'email',
            'whatsapp',
            'assunto',
            'mensagem',
        )

        widgets = {

            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seu nome',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'seu@email.com',
                }
            ),

            'whatsapp': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '(21) 99999-9999',
                }
            ),

            'assunto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Assunto',
                }
            ),

            'mensagem': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite sua mensagem...',
                    'rows': 6,
                }
            ),
        }


    def clean_nome(self):

        nome = self.cleaned_data['nome'].strip()

        if len(nome) < 2:

            raise forms.ValidationError(
                'Informe seu nome corretamente.'
            )

        return nome


    def clean_whatsapp(self):

        whatsapp = self.cleaned_data.get(
            'whatsapp',
            ''
        ).strip()

        # WhatsApp é obrigatório
        if not whatsapp:

            raise forms.ValidationError(
                'Informe seu WhatsApp.'
            )

        # Remove tudo que não seja número
        numeros = re.sub(
            r'\D',
            '',
            whatsapp
        )

        # Não permite menos de 10 números
        if len(numeros) < 10:

            raise forms.ValidationError(
                'Informe um WhatsApp válido com DDD.'
            )

        # Não permite mais de 11 números
        if len(numeros) > 11:

            raise forms.ValidationError(
                'Informe um WhatsApp válido com DDD.'
            )

        return whatsapp

