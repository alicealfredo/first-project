"""Implement a program that reads a number (between 1 and 99) and determines
its representation in binary language.
Example:
Number: 12 Result: 1 1 0 0
Number: 29 Result: 1 1 1 0 1
"""


num = int(input("Número: "))

if num < 1 or num > 99:
    print("Digite um número entre 1 e 99.")
else:
    binario = ""  

    n = num
    while n > 0:
        binario = str(n % 2) + binario 
        n = n // 2  

    print("Resultado:", " ".join(binario))
