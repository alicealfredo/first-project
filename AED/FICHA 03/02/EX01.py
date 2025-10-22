"""Analisador de texto estruturado
Implemente uma função que receba um texto (inserido pelo utilizador) e produza um relatório estatístico com:
• Número total de palavras;
• Palavra mais longa e palavra mais curta;
• Quantas palavras começam e terminam com a mesma letra;
• Quantas palavras aparecem mais de uma vez (e quais são elas,
com a contagem).
"""

def analisadorTexto(text):
    palavras = text.split()
    palavraLonga = palavras[0]
    palavraCurta = palavras[0]
    letrasIguais = 0

    for palavra in palavras:
        if len(palavra) > len(palavras):
            palavraLonga = palavra  
        elif len(palavra) < len(palavras):
            palavraCurta = palavra
    
        if palavra[0] == palavra[-1]:
            letrasIguais += 1
            print(palavra)
    
    print(f"Palavra mais longa: {palavraLonga}")
    print(f"Palavra mais curta: {palavraCurta}")
    print(f"Palavras que começam e terminam com a mesma letra: {letrasIguais}")



text = str(input("Digite um parágrafo: "))
analisadorTexto(text)


