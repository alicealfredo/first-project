// 1. 2. 3. O utilizador deve escolher um número, que deverá ser recolhido através de um prompt;
// Utilizando uma estrutura de repetição, calcula a tabuada do número escolhido;
// Para cada número da tabuada, fazer um console.log que siga a estrutura:
// a. “4 x 1 = 4”
// “4 x 2 = 8”
// “4 x 3 = 12”

let num = +prompt("Digite um número:"); // pede ao usuário 
for(let i=1; i<=10; i++){
    let tabuada = num * i
console.log(`${num}x${i}=${tabuada}`)
}