"""Develop a program that simulates the factorial function, that is, that
determines the factorial of a given number.
Example: Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120
Note that 0! = 1
Note: Do not use the math.factorial () function
The goal is to develop our own factorial function.
"""
numero = int(input("Indique um número: "))
fatorial = 1
for i in range(1,numero+1):
    fatorial *=i

print(f"Fatorial de {numero}: {fatorial}")