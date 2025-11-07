// O objetivo é desenvolver um programa que desafie o utilizador a adivinhar um número aleatório
// gerado pelo computador.
// O número aleatório deve ser um valor entre 1 e 10, e o programa deve indicar se o utilizar acertou à
// primeira, caso contrário, deve dizer quantas vezes seriam necessárias até sair o número escolhido.

let ale;
let num = 0;
let tent = 0;

while(num!=ale) {
    ale = Math.ceil(Math.random() * 10);
    num = +prompt("Escolha um número de 1 a 10:\n(Podes consultar na consola o número de tentativas necessárias)");
    tent++;
    console.log(`${tent}º tentativa - número gerado: ${ale}`);
    if(num!=ale) {
        alert("Não acertaste o número, tente novamente.");
    }
}

if(tent==1) {
     alert(`Parabéns! Acertou o número ${num} de primeira.`);
} else {
    alert(`Acertou o número ${num} em ${tent} tentativas.`);
}

