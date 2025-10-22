"""Create the function standardName(name) that should receive a full name
(based on as input) and returns a string with the normalized name: it
should include the first and last name (as in the previous exercise) and
abbreviations of all other intermediate names, such as in the example
bellow:
Example:
standardName('Carlos Alberto Costa Pereira') => Carlos A. C. Pereira
"""

def standardName(name):
    palavras = name.split() #split() para contar as palavras
    nome_final = palavras[0] + " "  #primeiro nome

    for i in range(1, len(palavras) - 1): # len(palavras) - 1 pois o último nome não conta como inicial
        nome_final += palavras[i][0] + ". " # adiciona iniciais dos nomes do meio
    
    nome_final += palavras[-1]  # último sobrenome completo

    return nome_final

name = str(input('Nome: '))
print(standardName(name))