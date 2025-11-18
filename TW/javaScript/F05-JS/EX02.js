// Números negativos e positivos

let numeros = [];
let numerosPositivos = [];
let numerosNegativos = [];

for (let i = 0; i < 15; i++) {
    let ale = Math.ceil(Math.random() * 100) - 50;
    numeros.push(ale);
    if(ale>0) {
        numerosPositivos.push(ale);
    } else if (ale<0) {
        numerosNegativos.push(ale);
    }
}

alert(`A lista continha os números ${numeros}, com ${numerosNegativos.length} números negativos e ${numerosPositivos.length} positivos.`)
