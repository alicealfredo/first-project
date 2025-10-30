"""
Create a program that allows you to generate a random number between [1-100] and
display it in the Console. Then your program should ask the user: "Do you want to gen-
erate a new number (S/N)?".
• If you answer No: end the program, displaying the list of all the numbers gener-
ated, in descending order;
• If you answer Yes: you must generate a new random number between the last
generated number +1, and 100
Notes:
• It must be ensured that the random numbers generated in the previous process
are never repeated;
• If the randomly generated number is equal to 100, you must finish the program by
displaying the list of all the generated numbers, in descending order
"""

import random

ale = random.randint(1, 100)
numerosGerados = []
numerosGerados.append(ale)
print(f"Número gerado: {ale}")

resposta = input("Deseja gerar um novo número? (S/N): ")

while resposta != "N":
    while ale < 100:
        novoAle = random.randint(ale + 1, 100)

        while novoAle in numerosGerados:
            novoAle = random.randint(ale + 1, 100)
        
        numerosGerados.append(novoAle)
        ale = novoAle
        print(f"Número gerado: {novoAle}")
        resposta = input("Deseja gerar um novo número? (S/N): ")