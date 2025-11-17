"""
Create an application that allows you to manage a country
file (paises.txt), with a structure like the one shown in the
example: country; continent
"""
import os
listaContinentes = ["Europa", "América", "África", "Ásia", "Oceania"]
fileName = "paises.txt"
filePath = "./files/"

fileName = filePath+fileName

def paisExiste(pais):
    filePaises = open(fileName, 'r')
    listaPaises = filePaises.readlines()
    filePaises.close()
    for linha in listaPaises:
        campos = linha.split(";")
        if campos[0] == pais:
            return True

def guardarFicheiro(pais,continente):
    filePaises = open(fileName, 'r')
    with open(fileName, 'a', encoding="utf-8") as filePaises:
        linha = pais + ";" + continente + "\n"
        filePaises.write(linha)
        filePaises.close()


def addCountry():
    pais = input("País: ")
    continente = input("Continente: ")
    filePaises = open(fileName, 'r')
    if continente not in listaContinentes:
        print("Continente não existe. Prima <enter> para continuar...")
        input()

    elif paisExiste(pais) == True:
        print("País já existe na lista. Prima <enter> para continuar...")
        input()
    else:
        guardarFicheiro(pais, continente)

    with open(fileName, 'a', encoding="utf-8") as filePaises:
        linha = pais + ";" + continente + "\n"
        filePaises.write(linha)
        filePaises.close()

def showCountries():
    filePaises = open(fileName, 'r', encoding="utf-8")
    for pais in filePaises:
        print(pais)
    filePaises.close()

option = ""
while option != 0:
    print("\n\n\tMENU")
    print("\t1 - Inserir países")
    print("\t2 - Consulta países")
    print("\t3 - Consulta por continente")
    print("\t4 - Consulta nº países")
    print("\t0 - Sair")
    option = int(input("\t\t\tOpção: "))
    if option == 1:
        addCountry()
    # elif option ==2:
    #     showCountries()
    # elif option == 3:
