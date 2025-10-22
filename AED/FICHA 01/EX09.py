"""Adapt your body mass index | índice de massa corporal(IMC) developed in point
4. After calculating and printing the IMC, your program should categorize
the individual, based on the IMC index obtained, according to the following
table:
IMC              Classification
<18.5            Abaixo do peso; low weight
18.5 - 24.9      Peso Normal; normal weight
25 - 29.9        Excesso de peso; overweight
30 - 34.9        Obesidade Grau I; grade I obesity
35 - 39.9        Obesidade Grau II; grade II obesity
>=40             Obesidade Mórbida; morbid obesity
"""

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

IMC = peso / (altura**2)

print("O seu IMC é: %.2f " % (IMC))

if IMC<18.5:
    print("Abaixo do peso")
elif IMC<=24.9:
    print("Peso Normal")
elif IMC<=29.9:
    print("Excesso de peso")
elif IMC<=34.9:
    print("Obesidade Grau I")
elif IMC<=39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Mórbida")