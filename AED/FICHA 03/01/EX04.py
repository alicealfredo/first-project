"""Write the removeSpaces(text) function that receives a text and replaces
sequences of two or more spaces with a single space. The function shoul
return the text normalized, with single spaces between words.
"""

def removeSpaces(texto):
    palavras = texto.split() #split() para contar as palavras ou .count(" ") para contar os vários espaços e substituir por um só
    resultado = ""
    for i in range(len(palavras)):
        resultado += palavras[i]
        if i < len(palavras) - 1:
            resultado += " "
    return resultado
            
text = str(input('Indique um texto: '))
print("Texto: ", removeSpaces(text))