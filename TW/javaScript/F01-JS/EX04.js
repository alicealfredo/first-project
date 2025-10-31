let op = prompt("Que operação desejas fazer? (+, -, * ou /)");
let num1 = +prompt("Escolha o primeiro número:");
let num2 = +prompt("Escolha o segundo número:");
let soma = num1 + num2;
let subtracao = num1 - num2;
let multiplicacao = num1 * num2;
let divisao = num1 / num2;

switch (op) {
    case "+":
        alert(num1 +"+"+ num2 +"="+ soma);
        break;
    case "-":
        alert(num1 +"-"+ num2 +"="+ subtracao);
        break;
    case "*":
        alert(num1 +"*"+ num2 +"="+ multiplicacao);
        break;
    case "/":
        alert(num1 +"/"+ num2 +"="+ divisao);
        break;
}