// - Devem ser percorridos todos os números de 1 até 10, inclusive;
// - O programa deve verificar quais desses números é par.
//      - A verificação deve ser feita dentro de uma função;
//      - A função deve receber e utilizar parâmetros;
//      - Se for par, a função deve dar return true;
// - Deve ser feito um console.log para cada número que for par.

function numPar(i) {
    if (i%2==0) {
        return true
    } else {
        return false
    }
}

for(let i = 1; i<= 10;i++) {
    numPar(i)
    if (numPar(i)==true) {
        console.log("O número " + i + " é par.");
        numPar(i);
    }
}