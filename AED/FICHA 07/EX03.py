"""
APPLICATION 3: CSV FILE
"""
import csv
import matplotlib.pyplot as plt

filePath = "./files/"
fileName = "carros_usados.csv"
fileName = filePath + fileName

marca = input("Indique a marca do carro: ")
listaDeMarcas = []
listaCarrosMarca = []


with open(fileName, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for linha in reader:
        marcaCarro = linha["Make"].lower()
        if marcaCarro != marca : continue
        if marcaCarro == "" : continue
        preco =float(linha["price"])

        listaCarrosMarca.append(preco) #preços dos carros da marca indicada

if listaCarrosMarca == []:
    print(f"Não foram encontrados carros da marca {marca}.")
else:
    print(f"Marca: {marca}")
    print(f"Máximo: {max(listaCarrosMarca):.2f}")
    print(f"Mínimo: {min(listaCarrosMarca):.2f}")
    print(f"Média: {(sum(listaCarrosMarca)/2):.2f}")

"""
Gráfico
"""

xpoints = []
for i in range(len(listaCarrosMarca)):
    xpoints.append(i)

ypoints = ([listaCarrosMarca])

plt.scatter(xpoints, ypoints)


