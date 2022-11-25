from django.urls import path
from . import views

#urlpatterns = [path('lista/', views.Reservas.as_view(),
# name='lista-reservas'),
#]

app_name = "Reservas"

urlpatterns = [
    path('cria/', views.ReservaCriar.as_view(), name='cria-reservas'),
    path('edita/', views.ReservaAtualizar.as_view(), name='atualiza-reservas'),
    path('edita/', views.ReservaApagar.as_view(), name='apaga-reservas'),
    path('', views.ReservaLista.as_view(), name='lista-reservas'),

]