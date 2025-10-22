"""Read a set of n integers (where n is previously specified by the user.
Then determine the second largest value among the set of numbers read.
Note: do not use arrays /lists to solve the exercise!
"""

n = int(input("Quantos números desejas ler? "))

num1 = int(input("Número: "))
num2 = int(input("Número: "))

if num1 > num2:
    maior = num1
    segundo_maior = num2
else:
    maior = num2
    segundo_maior = num1


for i in range(3, n + 1):
    num = int(input("Número: "))
    if num > maior:
        segundo_maior = maior
        maior = num
    elif num > segundo_maior:
        segundo_maior = num

print(f"O segundo maior valor informado é: {segundo_maior}")