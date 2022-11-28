from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls.base import reverse_lazy

#urlpatterns = [path('lista/', views.Reservas.as_view(),
# name='lista-reservas'),
#]

app_name = "Reservas"

urlpatterns = [
    path('cria/', views.ReservaCriar.as_view(), name='cria-reservas'),
    path('edita/<int:pk>/', views.ReservaAtualizar.as_view(), name='atualiza-reservas'),
    path('apaga/<int:pk>/', views.ReservaApagar.as_view(), name='apaga-reservas'),
    path('', views.ReservaLista.as_view(), name='lista-reservas'),

    path('login/', LoginView.as_view(template_name='Login/login.html'), name='login'),
    path('logout/', LogoutView.as_view( next_page=reverse_lazy('Login:login'), ), name='logout'),
    path('alterarSenha/', PasswordChangeView.as_view(template_name='Login/alterarSenha.html', success_url=reverse_lazy('Login:alterarOk'), ), name='alterarSenha'),
    path('alterarOk/', views.SenhaAlterada.as_view(), name='alterarOk'),
]