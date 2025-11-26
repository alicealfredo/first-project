"""
Create an application that allows you to manage a country
file (paises.txt), with a structure:
country;continent
"""
import os

listaContinentes = ["Europa", "América", "África", "Ásia", "Oceania"]

filePath = "./files/"
fileName = "paises.txt"
fileName = filePath + fileName

if not os.path.exists(filePath):
    os.makedirs(filePath)

# Função para verificar se o país já existe no ficheiro
def paisExiste(pais):
    try:
        filePaises = open(fileName, "r", encoding="utf-8")
        listaPaises = filePaises.readlines()
    except Exception as e:
        print("Erro ao abrir o ficheiro:", e)
        input()
        return True
    finally:
        filePaises.close()
    
    for linha in listaPaises:
        campos = linha.strip().split(";")
        if campos[0].lower() == pais.lower():
            return True
    
    return False

# Opção 1: Inserir países
def addCountry():
    pais = input("País: ").strip()
    continente = input("Continente: ").strip()

    if continente not in listaContinentes:
        print("Continente não existe. Prima <enter> para continuar...")
        input()
        return

    if paisExiste(pais):
        print("País já existe na lista. Prima <enter> para continuar...")
        input()
        return

    guardarFicheiro(pais, continente)
    print("País adicionado com sucesso! Prima <enter> para continuar...")
    input()

# Função para guardar país no ficheiro
def guardarFicheiro(pais, continente):
    with open(fileName, "a", encoding="utf-8") as filePaises:
        linha = pais + ";" + continente + "\n"
        filePaises.write(linha)

# Opção 2: Consulta países
def showCountries():
    filePaises = open(fileName, "r", encoding="utf-8")
    lista = filePaises.readlines()
    filePaises.close()

    print("\nPaís\t\tContinente")
    print("--------------------------------")
    for linha in lista:
            linha = linha.strip()
            campos = linha.split(";")

            if len(campos[0]) < 8: #para ajustar o espaçamento e manter alinhados os continentes
                print(campos[0] + "\t\t" + campos[1])
            else:
                print(campos[0] + "\t" + campos[1])

                
    print("\nPrima <enter> para continuar...")
    input()

# Opção 3: Consulta por continente
def consultaPorContinente():
    cont = input("Indique o continente: ").strip()
    cont_normalizado = cont.capitalize()

    filePaises = open(fileName, "r", encoding="utf-8")
    listaPaises = filePaises.readlines()
    filePaises.close()

    if cont_normalizado not in listaContinentes:
        print("Nenhum país encontrado.")
        return
    else:
        print("\nPaís\t\tContinente")
        print("--------------------------------")
        for linha in listaPaises:
            campos = linha.strip().split(";")

            if cont.lower() == campos[1].lower():
                
                if len(campos[0]) < 8: #para ajustar o espaçamento e manter alinhados os continentes
                    print(campos[0] + "\t\t" + campos[1])
                else:
                    print(campos[0] + "\t" + campos[1])

    print("\nPrima <enter> para continuar...")
    input()

# Opção 4: Consulta nº países por continente
def contaPaisesPorContinente():
    filePaises = open(fileName, "r", encoding="utf-8")
    lista = filePaises.readlines()
    filePaises.close()

    continentes = []
    contagens = []
    
    for linha in lista:
        pais, continente = linha.strip().split(";")
        
        if continente in continentes:
            indice = continentes.index(continente)
            contagens[indice] += 1
        else:
            continentes.append(continente)
            contagens.append(1)

    print("\nNúmero de países por continente:")
    print("----------------------------------")
    for i in range(len(continentes)):
        print(f"{continentes[i]}: {contagens[i]}")

    print("\nPrima <enter> para continuar...")
    input()

#  MENU
option = -1
while option != 0:
    os.system("clear")
    print("\n\n\tMENU")
    print("\t1 - Inserir países")
    print("\t2 - Consulta países")
    print("\t3 - Consulta por continente")
    print("\t4 - Consulta nº países por continente")
    print("\t0 - Sair")
    option = int(input("\t\t\tOpção: "))

    if option == 1:
        addCountry()
    elif option == 2:
        showCountries()
    elif option == 3:
        consultaPorContinente()
    elif option == 4:
        contaPaisesPorContinente()
    else:
        print("Opção inválida. Prima <enter> para continuar...")
        input()
