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

// CICLO FOR
let num5 = 5
for(let i=0; i<50; i++){
    num += 1
console.log(num5)
}

let person = {
    firstName: "Alice",
    lastName: "Moraes"
}
let fullName = ""
for(i in person){ // substitui por um número
    fullName += person[i]
    fullName += " "
    console.log(fullName);
}

 let arr = ["Laranjas", "bananas", "maças"]

 for (i of arr){ // busca o elemento da lista
    console.log(i)
 }

 let num6 = 50
 let i = 0

 while (num6 <= 55){
    num6++ // adicionar 1 à variável num6
    console.log(num6)
 }

 let cond = false
 do{ // Do/While faz sempre primeiro a condição antes de verificar se está falso ou verdadeiro
    console.log(cond);
 } while(cond == true)

let arr = [1, 5, 2, 11, 23] // Encontrar um número par numa lista
for(let i = 0; i < arr.length; i++){
    if(arr[i]%2==0){
        console.log(`O número ${arr[i]} é par`);
        continue
    }
}

// FUNÇÕES
function nomeFuncao(){
    return("Olá! Este é o return da função.")
}
let msg = nomeFuncao()
console.log(msg) // imprimir através de uma variável

function add(n1,n2 = 3) { // Passar parâmetros para a função (n2 = 3 assume o valor 3 caso não receba uma segunda variável)
    let sum = n1 + n2
    return sum
}
console.log(add(10,12))

function teste(...params) { // Cria uma lista com os parâmetros que recebe
    console.log(params)
}
teste(5,"Alice",true)

// Função Anónima
let nome = function() {
    console.log("Alice")
}
nome()

// Funções Arrow
let sum = (a,b) => a + b // recebe dois parâmetros e imprime a soma
console.log(sum(2,4))

