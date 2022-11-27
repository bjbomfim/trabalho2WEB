function mostrarLista() {
    var display = document.getElementById("lista")
    if (display == "none")
        document.getElementById("lista").style.display = 'block';
    else
        document.getElementById("lista").style.display = 'none';
}