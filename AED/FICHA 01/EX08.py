"""Write a program that implements an Ideal Weight Simulator.
The algorithm should ask the user for their gender (M for male and F for
female) and height (in cm).
The simulation of ideal weight (Peso Ideal) is given by the following formula: Ideal weight = (h-100) - (h-150)/k
Whereas: k = 2 for females and k = 4 for males (h is the height in cm)
"""
genero=input("Indique o sexo (F/M): ")
altura=int(input("Indique a altura (cm): "))

pesoIdeal=(altura-150)

if genero=="f" or genero=="F":
    print(f"O peso ideal é {(altura-100)-pesoIdeal/2} kg.")
elif genero=="m" or genero=="M":
    print(f"O peso ideal é {(altura-100)-pesoIdeal/4} kg.")
else:
    print("Opção Inválida.")