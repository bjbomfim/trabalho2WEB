function mostrarLista() {
    var tabelaConteudo = document.getElementsByClassName("lista");
    var botao = document.getElementById("botaoLista");
    for(i=0;i<tabelaConteudo.length;i++){
        if (tabelaConteudo[i].hidden == true){
            tabelaConteudo[i].hidden = false;
            botao.innerText = "Esconder lista";
        }else{
            tabelaConteudo[i].hidden = true;
            botao.innerText = "Exibir lista";
        }
    }

    
}

