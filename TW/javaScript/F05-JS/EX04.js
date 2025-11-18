// Implemente um pequeno sistema de autenticação com prompt() e alert().

let userName = prompt("Username:");

if (userName == "Admin") {
    let password = prompt("Password:")
    if (password == "TheMaster") {
        alert("Bem-vindo!");
    } else if (password == "") {
        alert("Cancelado");
    } else {
        alert("Password errada");
    }
} else if (userName == "") {
    alert("Cancelado");
} else {
    alert("Username não reconhecido");
}