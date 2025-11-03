// - O programa deve pedir um número ao utilizador através de um prompt;
// - Verifica se o número introduzido é um número primo, isto deve estar dentro de uma função;
// - Apresenta a conclusão num alert.

let num = +prompt("Digite um número:");

function numPrimo (num) {
    for(let i = 3; i<=num; i++) {
        if(num%i==1) {
            alert("O número " + num + " não é primo.");
        } 
        else {
            alert("O número " + num + " é primo.");
        }
    }
}

numPrimo()
