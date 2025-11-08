// O objetivo é desenvolver o código JavaScript necessário para que o utilizador receba um username
// com base nos dados fornecidos.

let nome = prompt("Nome:");
let apelido = prompt("Apelido:");
let num = +prompt("Escolha um número entre 0 e 100:");

nome = (nome[0]).toUpperCase() + nome.slice(1, 3)
apelido = (apelido[0]).toUpperCase() + apelido.slice(1, 3)

let userName = nome + apelido + num;

alert(`O teu username é ${userName}`);
