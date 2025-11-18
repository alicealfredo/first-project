let pratosPrincipais = document.getElementsByTagName("li");
for (let i=0; i<pratosPrincipais.length; i++) {
    console.log(pratosPrincipais[i]);
}

let btn = document.getElementsByTagName("button");
btn[0].addEventListener("click", function(){
    let prato = prompt("Qual prato desejas adicionar?");
    document.getElementById("pratos").innerHTML += `<li>${prato}</li>`
});

let titulo = document.getElementById("titulo");
titulo.addEventListener("mouseover", function(){
    document.getElementById("titulo").innerHTML = "Seja bem-vindo, faça-nos uma visita."
});
titulo.addEventListener("mouseout", function(){
    document.getElementById("titulo").innerHTML = "Menu do restaurante Tomatino"
});

