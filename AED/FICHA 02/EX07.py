"""Write a program that checks if a given number (integer and positive) is
perfect.
In mathematics, a perfect number is an integer for which the sum of all
its proper positive divisors is equal to the number itself.
For example, the number 6 is a perfect number because:
6 is divisible by: 1, 2 and 3. And 1+2+3 = 6, therefore it is a perfect number
"""

num = int(input("Introduza um número inteiro: "))

if num<0:
    print("O número a indicar deve ser >=0")
    exit()

somaDiv = 0

for i in range(num-1, 0,-1):
    if num % i == 0:
        somaDiv += i

if somaDiv == num:
    print(f"{num} é um número perfeito.")
else:
    print(f"{num} não é um número perfeito.")
