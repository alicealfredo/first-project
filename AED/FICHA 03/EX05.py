"""Write the function shortName(name) that should receive a full name (based
on an input) and return a string with the first and last name (first given
name and last surname).
Example:
shortName('Manuel Jorge da Costa Pereira') => Manuel Pereira
"""

def shortName(name):
    contador = name.split() #split() para contar as palavras
    nomeFinal = contador[0] + " " + contador[-1] #contador[-1] = apelido (começa a contar do fim para o início da palavra)
    return nomeFinal 


nome = str(input('Nome: '))
print(shortName(nome))