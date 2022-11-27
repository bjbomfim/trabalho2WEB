from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Morador(models.Model):
    apartamento = models.CharField(max_length=6)
    morador = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    firstAccess = models.BooleanField()
    def __str__(self) -> str:
        return self.apartamento

class Reserva(models.Model):
    dataReserva =  models.DateField(help_text='Data da Reserva')
    obs = models.CharField(max_length=300, help_text='Insira o motivo da reserva')
    apartamento = models.ForeignKey(Morador, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.obs


