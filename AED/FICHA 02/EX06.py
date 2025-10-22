"""Develop a program that illustrates the first n terms of the Fibonacci
sequence, where the number of desired terms (n) must be indicated by the
user.
Fibonacci sequence , each term results from the sum of the two previous ones.
Source: http://pt.wikipedia.org/wiki/N%C3%BAmero_de_Fibonacci
"""
num = int(input("Nº de termos a imprimir: "))
num1 = 0
num2 = 1

print(f"Os {num} primeiros termos da sequência de Fibonacci:")

for i in range(num):
    if i == num - 1:
        print(num1) 
    else:
        print(num1, end=" ")
    proximo = num1 + num2
    num1 = num2
    num2 = proximo
