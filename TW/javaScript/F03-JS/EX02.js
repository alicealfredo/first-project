// O objetivo deste exercício é consolidar os conhecimentos sobre estruturas de decisão e eventos,
// passando informação ao utilizador sobre a situação escolar de um determinado aluno.

function avaliacao() {
    let ale = Math.ceil(Math.random() * 20);
    let resultado;
    if (ale<=9) {
        resultado = "em Negativa";
    } else if (ale>9 && ale<=13) {
        resultado = "na necessidade de ir à Prova Oral";
    } else if (ale>13 && ale<=17) {
        resultado = "em Positiva";
    } else if (ale>17 && ale<=20) {
        resultado = "em Excelente";
    }
    
    alert(`O estudante teve ${ale} valores, resultando ${resultado}`);
}