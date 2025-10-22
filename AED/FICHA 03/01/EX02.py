"""Implement the countText(text) function. The function should receive a
text, based on an input, and should print:
• The number of characters
• The number of spaces
• The number of vowels
Included in this text.
"""

text = str(input('Indique um texto: '))
vogais="aeiou"
espacos= text.count(" ")

def countText(text,vogais,espacos):
    print(f"Nº de caracteres: {len(text)}")
    for caracter in text:
        for i in range(0,len(text)):
            if text[i].lower() in vogais:
                vogais += 1
    print(f"Nº de vogais: {vogais}")
    print(f"Nº de espaços: {espacos}")

    return vogais, espacos

countText(vogais,espacos)
        