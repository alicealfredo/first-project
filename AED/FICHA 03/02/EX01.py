"""Analisador de texto estruturado
Implemente uma função que receba um texto (inserido pelo utilizador) e produza um relatório estatístico com:
• Número total de palavras;
• Palavra mais longa e palavra mais curta;
• Quantas palavras começam e terminam com a mesma letra;
• Quantas palavras aparecem mais de uma vez (e quais são elas,
com a contagem).
"""

def analisadorTexto(text):
    letras = 0
    palavras = text.split()
    palavraLonga = 0
    for i in range(0,len(text)):
        if text[i] in text:
            letras += 1
        for i in range(0,len(palavras)):
            if palavraLonga < palavras[i]:
                palavraLonga = palavras[i]
                  
    return palavraLonga
text = str(input("Digite um parágrafo: "))
print(analisadorTexto(text))

