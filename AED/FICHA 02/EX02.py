"""Implement a program that asks the user to indicate 2 integers (lower
limit and upper limit), then calculates the sum of all pairs between
that range (including the indicated limits).
Example:
Lower limit: 1
Upper limit: 10
Sum of pairs in the range = 2+4+6+8+10=30
"""
limInf=int(input("Limite Inferior: "))
limSup=int(input("Limite Superior: "))
soma = 0
for i in range(limInf,limSup+1):
    if i%2 ==0:
        soma+=i

print(f"A soma de todos os números pares entre {limInf} e {limSup} é {soma}")