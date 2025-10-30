"""
Develop a program that reads a list of 10 integers (validate with exceptions). The list may
contain duplicate values.
Then, given a certain search value (by input),call a function named searchNumber () that
should return the positions where it finds the search value in the list.
If the search value does not exist in the list, a suitable message should appear.
"""

def searchNumber(lista,valorPesquisa):
    if valorPesquisa in lista:
        cont = lista.count(valorPesquisa)
        if cont>1:
            for i in range(len(lista)):
                if lista[i]==valorPesquisa:
                    posicao = " " + str(i+1)
                
        else:
            posicao = lista.index(valorPesquisa)+1
            return posicao
    else:
        print("Valor não encontrado na lista.")

try:
    lista = []
    for i in range(10):
        valor =int(input(f"{i+1}º Número: "))

except ValueError:
    print("Insira um valor inteiro válido.")
else:
    lista.append(valor)

valorPesquisa = int(input("Valor de pesquisa: "))
posicao = searchNumber(lista,valorPesquisa)
print(f"O valor {valorPesquisa} existe na lista na(s) posição(ões) {posicao}")