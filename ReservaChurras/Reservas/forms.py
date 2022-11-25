from django import forms
from Reservas.models import Reserva


class ContatoModel2Form(forms.ModelForm):
    dataReserva = forms.DateField(input_formats=['%d/%m/%Y'], label='Data da Reserva', help_text='Reserva no formato DD/MM/AAAA',)
    class Meta:
        model = Reserva
        fields = '__all__'