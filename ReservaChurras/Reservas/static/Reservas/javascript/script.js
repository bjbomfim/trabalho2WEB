function mostrarLista() {
    var tabelaConteudo = document.getElementById("lista");
    var botao = document.getElementById("botaoLista");
    if (tabelaConteudo.style.display == "none"){
        tabelaConteudo.style.display = 'contents';
        botao.innerText = "Esconder lista";
    }else{
        tabelaConteudo.style.display = 'none';
        botao.innerText = "Exibir lista";
    }
}