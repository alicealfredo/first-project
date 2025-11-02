let num = 5 // indicar uma variável
console.log(num); // imprimir variável
// Keywords não podem ser usadas como nomes de variáveis (let let = 10)

// ---- Condições: ---- //

// IF
let num2 = 10
if(num%2==0){
    console.log("Número par");
}
else {
    console.log("Número ímpar");
    }

// SWITCH
let dia = "domingo"

switch(dia){
    case "domingo":
        console.log("1 dia");
        break;
    case "segunda":
        console.log("2 dia");
        break
}

// Incremento: nomeVariavel ++

// ---- Input ---- //
let num3 = +prompt("Escolha um número:");
let num4 = +prompt("Escolha outro número:");
console.log(num3, num4); // imprimir no console
alert(num3,num4); // aparecer em formato de alerta como pop-up

