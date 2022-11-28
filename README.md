# Relatório

:man_technologist:	Alexandre R. Bomfim Jr. - 1921241
:man_technologist:	José Lucas Teixeira Xavier - 1921254

Endereço do site: http://alexandrebejota.pythonanywhere.com/

# O Site

Desenvolvemos um site fictício de agendamento/reserva da churrasqueira do Hotel Copacaba Palace. 

# Requisitos pedidos para o site

  :heavy_check_mark: Fazer uso do framework web Django para o desenvolvimento do site
 <br/> :heavy_check_mark: Aplicar HTML, CSS e Javascript no site desenvolvido
 <br/> :heavy_check_mark: Conter as quatro operações básicas em banco de dados (CRUD)
 <br/> :heavy_check_mark: Ser publicado em um provedor de serviço Web
 <br/> :heavy_check_mark: Usar Git para controle de versão e armazenado em um provedor de repositório Git de acesso público
 <br/> :x: Realizar push semanalmente
 <br/> :x: Fazer uso do AJAX no site
 <br/> :heavy_check_mark: Login, acesso e/ou ações selecionadas por usuário. Cada usuário deverá ter visões diferentes do site

# Funcionamento do site

A primeira tela mostrado ao usuário, após ele adentrar o link do site, será a tela de Login, onde através dela o mesmo preencherá seu usuário e senha para acessar as funcionalidades disponíveis do site. Contudo, neste site apenas os hóspedes(usuários cadastrados no banco) podem entrar no site, e assim realizar um agendamento para a churrasqueira.
<br/>Após realizar o login, tendo sucesso na validação do banco, o usuário se adentrará no site, onde exergará como a página inicial sendo a de lista de reserva que foi feita pelo usuário (login: teste1, senha: teste12345678). Nesta página, o usuário poderá tomar algumas ações, como por exemplo a de inserir uma reserva.
<br/>Neste inserção de reserva, é obrigatório botar uma observação do que se trata o motivo do agendamento e também inserir a data que o hóspede/usuário deseja reservar a churrasqueira. Com isso, o sistema insere o agendamento no banco de dados, o qual vai ficar vinculado diretamente com o apartamento do usuário que realizou a reserva. 
<br/>Após realizar a reserva, a mesma irá aparecer na página inicial na lista de reservas do usuário, onde ele ficará apto a atualizar a reserva que foi feita, ou seja, realizar alguma alteração de data ou motivo nessa reserva. 
<br/>Outra funcionalidade permitida após a criação de uma reserva, será a exclusão, onde que nela o usuário poderá excluir uma reserva feita anteriomente por ele. Ao clicar no botão de excluir, o site vai apresentar a pergunta de confirmação se ele deseja excluir ou não a reserva que foi clicada, e assim cabe ao usuário decidir qual ação será tomada.


