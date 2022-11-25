from django.db import models

# Create your models here.
class Reserva(models.Model):
    dataReserva =  models.DateField(primary_key=True, serialize=False, help_text='Data da Reserva')
    obs = models.CharField(max_length=300, help_text='Insira o motivo da reserva')

    def __str__(self) -> str:
        return self.obs

