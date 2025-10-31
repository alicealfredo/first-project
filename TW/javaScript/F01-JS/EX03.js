let peso = +prompt("Digite seu peso (kg):");
let altura = +prompt("Digite sua altura (m):");
let imc = peso / (altura * altura);

if(imc < 18.5){
    alert("Magreza");
}
else if(imc >= 18.5 && imc < 24.9){
    alert("Normal");
}
else if(imc >= 25 && imc < 29.9){
    alert("Sobrepeso");
}
else if(imc >= 30 && imc < 34.9){
    alert("Obesidade grau I");
}
else if(imc >= 35 && imc < 39.9){
    alert("Obesidade grau I");
}
else {
    alert("Obesidade grau III");
}