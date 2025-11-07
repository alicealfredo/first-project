let ale = Math.ceil(Math.random() * 10);
let num = 0;
let tent = 0;

while(num!=ale) {
    alert("Podes consultar na consola (DevTools) o número de tentativas necessárias");
    num = +prompt("Escolha um número (de 1 a 10): ");
    alert(ale);
    tent++;
    console.log(`${tent}º tentativa - número gerado: ${ale}`);
}

if(tent==1) {
     alert(`Parabéns! Acertou o número ${num} de primeira.`);
} else {
    alert(`Acertou o número ${num} em ${tent} tentativas.`);
}

