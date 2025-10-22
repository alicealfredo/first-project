"""Escreva um pequeno programa que calcule o seu peso ideal
Neste exercício vamos usar (para já!) um algoritmo de cálculo simplificado,
baseado apenas na sua altura, de acordo com a fórmula:
Peso ideal = (altura-100) * 0.9
"""

altura = float(input("Altura em cm: "))
pesoIdeal = (altura - 100) * 0.9

print("Peso ideal %.1f kg" % (pesoIdeal))
