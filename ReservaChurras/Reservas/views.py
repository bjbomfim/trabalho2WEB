from django.shortcuts import render
from Reservas.models  import Reserva
from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404
from Reservas.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.

class ReservaLista(View):
    def get(self, request, *args, **kwargs):
        reservas = Reserva.objects.all()
        contexto = { 'reservas': reservas, }
        return render(request,'Reservas/home.html', contexto)

class ReservaCriar(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': ContatoModel2Form, }
        return render(request,"Reservas/inserirReserva.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = ContatoModel2Form(request.POST)
        if formulario.is_valid():
            reserva = formulario.save()
            reserva.save()
        return HttpResponseRedirect(reverse_lazy('Reservas:lista-reservas'))

class ReservaApagar(View):
    def get(self, request, pk, *args, **kwargs):
        reserva = Reserva.objects.get(pk=pk)
        contexto = { 'reserva': reserva, }
        return render(request, 'Reservas/apagaReserva.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        reserva = Reserva.objects.get(pk=pk)
        reserva.delete()
        return HttpResponseRedirect(reverse_lazy("Reservas:lista-reservas"))

class ReservaAtualizar(View):
    def get(self, request, pk, *args, **kwargs):
        reserva = Reserva.objects.get(pk=pk)
        formulario = ContatoModel2Form(instance=reserva)
        contexto = {'reserva': formulario, }
        return render(request, 'Reservas/atualizaReserva.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        reserva = get_object_or_404(Reserva, pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=reserva)
        if formulario.is_valid():
            reserva = formulario.save() 
            reserva.save()
            return HttpResponseRedirect(reverse_lazy("Reservas:lista-reservas"))
        else:
            contexto = {'reserva': formulario, }
            return render(request, 'Reservas/atualizaReserva.html', contexto)



