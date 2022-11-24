from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Reservas/home.html')

def segundaPagina(request):
    return render(request, 'Reservas/segunda.html')