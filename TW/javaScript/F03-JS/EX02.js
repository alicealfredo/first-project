// O objetivo deste exercício é consolidar os conhecimentos sobre estruturas de decisão e eventos,
// passando informação ao utilizador sobre a situação escolar de um determinado aluno.

function avaliacao() {
    let ale = Math.ceil(Math.random() * 20);
    let resultado;
    if (ale<=9) {
        resultado = "negativa";
    } else if (ale>9 && ale<=13) {
        resultado = "tem de ir a Prova Oral";
    } else if (ale>13 && ale<=17) {
        resultado = "positiva";
    } else if (ale>17 && ale<=20) {
        resultado = "excelente";
    }
    
    alert(`O estudante teve ${ale} valores, resultando em ${resultado}`);
}