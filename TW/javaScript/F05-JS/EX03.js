// Criar um programa em JavaScript que percorra uma lista de números e indique, para cada um, se é ou
// não uma capicua.

let numeros = [121, 123, 44, 456, 11, 90, 909, 22];

for (let num of numeros) {
    let invertido = num.toString().split('').reverse().join('');
    if (num == invertido) {
        console.log(`O número ${num} é capicua.`);
    } else {
        console.log(`O número ${num} não é capicua.`);
    }
}