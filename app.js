function sortear() {
    let quantidade = parseInt(document.getElementById('quantidade').value);
    let de = parseInt(document.getElementById('de').value);
    let ate = parseInt(document.getElementById('ate').value);

   
    let numero = obterNumeroAleatorio(de, ate);
    alert(numero);

}

function obterNumeroAleatorio(min, max) {

}
