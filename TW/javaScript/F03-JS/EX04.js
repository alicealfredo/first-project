// Neste exercício devem ser pedidos nomes, para que sejam organizados por ordem alfabética.

nome1 = prompt("Nome 1:");
nome2 = prompt("Nome 2:");
nome3 = prompt("Nome 3:");

nomes = [nome1, nome2, nome3];

let ultimo = (nomes.sort()).pop();
let texto = nomes.join(", ") + " e " + ultimo;

alert(texto);

