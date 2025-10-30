"""
Create a generateEuromillionKeys() function that allows you to generate Euromillions
keys randomly (5 integers between 1 and 50, as well as the stars: two stars between 1
and 12).
• Note that the numbers and stars in a key cannot be repeated.
• The function should return a key ordered (5 numbers and 2 stars)
• At the end, print the generated key and ask the user if he wants to generate a new
key (S/N).
"""
import random

def generateEuromillionKeys():
    chaveEuro = []
    for i in range(5):
        ale1 = random.randint(1,50)
        while ale1 in chaveEuro:
            ale1 = random.randint(1,50)
        chaveEuro.append(ale1)
        
    estrelas = []
    for j in range(2):
        ale2 = random.randint(1,12)
        while ale2 in estrelas:
            ale2 = random.randint(1,12)
        estrelas.append(ale2)
    
    print(f"Chave do Euromilhões: {chaveEuro}       Estrelas: {estrelas}")

generateEuromillionKeys()
resposta = input("Deseja gerar uma nova chave? (S/N): ")

while resposta.upper() == "S":
    generateEuromillionKeys()
    resposta = input("Deseja gerar uma nova chave? (S/N): ")
