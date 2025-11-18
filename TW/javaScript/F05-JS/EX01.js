// Crie um programa que simule um jogo de Bingo.

let numeros = [];
let numerosTirados = [];

for (let i=0; i<=90; i++) {
    numeros.push(i);
}

function tirarNumero() {
    if (numeros.length == 0) {
        alert("Todos os números foram tirados! A recomeçar...")
        numeros = [];
        numerosTirados = [];
        for (let i=0; i<=90; i++) {
            numeros.push(i);
        }
    } else {
        let posicaoAle = Math.ceil(Math.random() * numeros.length);
        alert(numeros[posicaoAle]);
        numeros.pop(numeros[posicaoAle]);
        numerosTirados.push(numeros[posicaoAle]);
    }
}

function bingo() {
    if (numerosTirados.length >= 15) {
        numeros = [];
        numerosTirados = [];
        for (let i=0; i<=90; i++) {
            numeros.push(i);
        }
    } else {
        alert("Impossível, continue.")
    }
}

