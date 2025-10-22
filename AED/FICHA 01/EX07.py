"""Implement a program that works as a small stress cardiac simulator, when
an athlete develops physical activity.
Your simulator should print the FCM (Frequência Cardiaca Máxima | Maximum
Heart Rate) based on gender and age, such as:
• feminine gender: FCM = 226 - age bpm (heartbeats per minute)
• masculine gender: FCM = 220 - age bpm (heartbeats per minute)
"""

genero=input("Indique o sexo (F/M): ")
idade=int(input("Indique a idade: "))

FCMF=226-idade
FCMM=220-idade

if genero=="F" or genero=="f":
    FCM=226-idade
    print(f"FCM={FCMF} bpm")
elif genero=="M" or genero=="M":
    print(f"FCM={FCMM} bpm")
else: 
    print("Opção Inválida")