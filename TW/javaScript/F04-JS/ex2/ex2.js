// O jogo Euromilhões consiste na extração de cinco números de uma esfera com 50 bolas numeradas
// de 1 a 50, e de duas estrelas de outra esfera com 12 bolas numeradas de 1 a 12.

let listaNum = [];
let listaEst = [];

while(listaNum.length <     5) {
    let ale = Math.ceil(Math.random() * 50);
    for(i = 0; i<listaNum.length; i++) {
        if (listaNum[i]!=ale) {
            console.log(ale);
            listaNum.push(ale);
        }
    }
}

// while(listaEst.length<2) {
//     let estrela = Math.ceil(Math.random() * 12);
//     console.log(estrela);
//     listaEst.push(estrela);
// }

alert(`- Chave do Euromilhões -\nNúmeros: ${listaNum.sort((a, b) => a - b)}`)