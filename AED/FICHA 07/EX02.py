"""
APPLICATION 2: BYNARY FILE 
"""
import os

filePath = "./files/"
fileName = "text.bin"
fileName = filePath + fileName

"""
Função que escreve o texto num ficheiro binário
"""
def writeText(text):
    with open(fileName, "wb") as file:
        file.write(text.encode("utf-8"))  # Converte o texto para bytes

    print("Texto gravado com sucesso em text.bin!")

"""
Função que lê o texto do ficheiro binário
"""
def readText():
    if not os.path.exists(fileName):
        print("O ficheiro text.bin não existe!")

    try:
        with open(fileName, "rb") as file:
            data = file.read()  # Ler os dados em bytes
            text = data.decode("utf-8") # Converter bytes novamente para texto
            return text #devolve em string

    except Exception as e:
        print("Ocorreu um erro ao ler o ficheiro:", e)

opcao = 1

while opcao != 0:
    print("\n")
    print("BINARY FILE")
    print("1 - Escrever texto no ficheiro")
    print("2 - Ler texto do ficheiro")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        texto = input("Texto:")
        writeText(texto)

    elif opcao == 2:
        conteudo = readText()
        print("\nConteúdo do ficheiro:")
        print(conteudo)

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")
