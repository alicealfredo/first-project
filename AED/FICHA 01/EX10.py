"""Implement a simulator of your weight on another planet!
The program should read your weight on Earth, as well as the planet identifier
code (between 1 and 6), and then calculate your weight on that planeta
according to the following table:
Code planet   Planet           Fator weight
1             Mercury           0.37
2             Venus             0.90
3             Mars              0.37
4             Jupiter           2.53
5             Saturn            1.06
6             Uranus            0.91
"""

print("\t\t\tPlanetas:\n\t\t1 - Mercúrio\n\t\t2 - Venus\n\t\t3 - Marte\n\t\t4 - Júpiter\n\t\t5 - Saturno\n\t\t6 - Urano")
print("\n")
peso = float(input("Peso (kg): "))
planeta = int(input("Indique o código do planeta: "))
pesoPlaneta = peso/0.98

match planeta:
    case 1:
        print(f"O seu peso de {peso} kg no planeta {planeta} seria de {pesoPlaneta*0.37:.2f} Kg")
    case 2:
        print(f"O seu peso de {peso} kg no planeta {planeta} seria de {pesoPlaneta*0.90:.2f} Kg")
    case 3:
        print(f"O seu peso de {peso} kg no planeta {planeta} seria de {pesoPlaneta*0.37:.2f} Kg")
    case 4:
        print(f"O seu peso de {peso} kg no planeta {planeta} seria de {pesoPlaneta*2.53:.2f} Kg")
    case 5:
        print(f"O seu peso de {peso} kg no planeta {planeta} seria de {pesoPlaneta*1.06:.2f} Kg")
    case 6:
        print(f"O seu peso de {peso} kg no planeta {planeta} seria de {pesoPlaneta*0.91:.2f} Kg")
    case _:
        print("Código de Planeta Inválido")