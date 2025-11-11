// Neste exercício vais criar um pequeno programa que permite ao utilizador gerir uma lista de compras,
// adicionando e removendo alimentos ou ingredientes conforme desejar. O utilizador pode ainda
// consultar a lista completa a qualquer momento.

let listaAli = [];

function adicionarAli() {
    let ali = (prompt("Qual alimento desejas adicionar?")).toLowerCase();
    
    if (listaAli.indexOf(ali) !== -1) { // Se o valor não existir, retorna -1
        alert(`${ali} já se encontra na lista de compras.`);
    } else {
        listaAli.push(ali);
        console.log(listaAli);
    }
}

function removerAli() {
    let removerAli = (prompt("Qual alimento desejas remover?")).toLowerCase();

    if (listaAli.indexOf(removerAli) == -1) { 
        alert(`${removerAli} não se encontra na lista de compras.`);
    } else {
        listaAli.pop(removerAli);
        console.log(listaAli);
    }
}

function verificarLista() {
    if (listaAli.length<1) {
        alert(`Alimentos: Não há alimentos na lista de compras`);
    } else {
        alert(`Alimentos: ${listaAli}`);
    }
}