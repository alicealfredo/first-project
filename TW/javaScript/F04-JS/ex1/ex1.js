// O objetivo é desenvolver o código JavaScript necessário para permitir que o utilizador some quantos
// números quiser, sendo que cada número introduzido é apenas de um dígito (de 0 a 9).

let listaNum =[];
let soma = 0;

function num(a) {
    listaNum.push(a);
    console.log(listaNum);
}

function resultado() {
    for (let i in listaNum) {
        soma = soma + listaNum[i];
    }
    alert(soma);
}