"""Write a program that reads an integer and determines whether that number
is even or odd (par ou ímpar).
"""

numero1 = int(input('Introduza um número inteiro: '))

r=numero1%2

if r==0:
    print(f"O {numero1} é um número par.")
else:
    print(f"O {numero1} é um número ímpar.")