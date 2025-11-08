// Neste exercício deve-se contar as vogais presentes na frase fornecida pelo utilizador, através de ciclos e funções.

let frase = (prompt("Escreva uma frase:")).toUpperCase();
let vogais = ["A","E","I","O","U"];
let contadorVogais = [];

let i=0;
while (i<vogais.length) {
    let contador = 0;
    for (let j in frase) {
        if (frase[j] == vogais[i]) {
            contador++;
        }
    }
    contadorVogais.push(` ${vogais[i]}: ${contador}`)
    i++;
}

alert(contadorVogais);