// O objetivo é desenvolver o código JavaScript necessário para que o utilizador receba um username
// com base nos dados fornecidos.

let nome = prompt("Nome:");
let apelido = prompt("Apelido:");
let num = +prompt("Escolha um número entre 0 e 100:");

let userName = (nome.slice(0,3) + apelido.slice(0,3)).toUpperCase() + num;

alert(`O teu username é ${userName}`);