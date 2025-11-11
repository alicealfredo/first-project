// O jogo Euromilhões consiste na extração de cinco números de uma esfera com 50 bolas numeradas
// de 1 a 50, e de duas estrelas de outra esfera com 12 bolas numeradas de 1 a 12.

let listaNum = [];
let listaEst = [];

while(listaNum.length < 5) {
    let ale = Math.ceil(Math.random() * 50);
    if (listaNum.indexOf(ale) === -1) { // Se o valor não existir, retorna -1
        console.log(ale);
        listaNum.push(ale);
    }
}

while(listaEst.length<2) {
    let est = Math.ceil(Math.random() * 12);

    if (listaEst.indexOf(est) === -1) { // Se o valor não existir, retorna -1
        console.log(est);
        listaEst.push(est);
    }
}

alert(`- Chave do Euromilhões -\n Números: ${listaNum.sort((a, b) => a - b)}\n Estrelas: ${listaEst.sort((a, b) => a - b)}`)