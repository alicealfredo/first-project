"""Write a program that reads a number (integer and positive) and indicates whether it is a prime number or not.
Note: A prime number is divisible only by itself and 1.
"""

num = int(input("Número: "))

if num <= 1:
    print(f"{num} NÃO É um número primo.")
else:
    contador = 0  
    for i in range(2, num):
        if num % i == 0:
            contador += 1  

    if contador == 0:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} NÃO É um número primo.")
