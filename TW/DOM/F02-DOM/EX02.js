let formulario = document.querySelector("#formulario");

console.log("Nome\t\tIdade\t\tCurso");
formulario.addEventListener("submit", function(event) {
    event.preventDefault();
    let nome = document.querySelector("#nome").value;
    let idade = document.querySelector("#idade").value;
    let curso = document.querySelector("input[name='option']:checked").value;
    
    console.log(nome+"\t\t"+idade+"\t\t\t"+curso);
});