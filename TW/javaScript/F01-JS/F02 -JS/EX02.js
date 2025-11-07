// - O programa deve pedir um número ao utilizador através de um prompt;
// - Verifica se o número introduzido é um número primo, isto deve estar dentro de uma função;
// - Apresenta a conclusão num alert.

let num = +prompt("Digite um número:");

function numPrimo (num) {
    let divisores = 0;

    for(let i = 3; i<=num; i++) {
        if(num%i==0) {
            divisores++;
        } else {
            divisores = 2;
        }
    }
    return divisores
}

numPrimo(num)

let divisores = numPrimo (num)

if(divisores!=2) {
    alert("O número " + num + " é primo.");
} else {
    alert("O número " + num + " não é primo.");
}