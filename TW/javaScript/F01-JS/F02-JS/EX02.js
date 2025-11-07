// - O programa deve pedir um número ao utilizador através de um prompt;
// - Verifica se o número introduzido é um número primo, isto deve estar dentro de uma função;
// - Apresenta a conclusão num alert.

let num = +prompt("Digite um número:");

function numPrimo(num) {
    if (num < 2) {
        return false;
    } else{
        for (let i = 2; i < num; i++) {
            if (num % i === 0) {
                return false;
            }
        }
    }
    return true;
}

if (numPrimo(num)==true) {
    alert("O número " + num + " é primo.");
} else {
    alert("O número " + num + " não é primo.");
}
