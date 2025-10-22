"""Make a 2.0 version of the previous game where:
After completing a game, the user should be given the option to start
a new game: “ New game (Y/N)?”.
The program must behave according to the response given by the user (
Y or N ).
"""

import random

def jogo():
    ale = random.randint(1, 50)
    tent = 1
    while tent <= 10:
        resp = int(input(f"Digite seu {tent}º palpite: "))
        if resp < ale:
            print("O número é MAIOR")
        elif resp > ale:
            print("O número é MENOR")
        else:
            print(f"Parabéns! Você adivinhou o número em {tent} tentativas!")
            break
        tent += 1
    else:
        print(f"Você usou todas as 10 tentativas. O número era {ale} :(")

while True:
    jogo()
    nJogo = input("Novo Jogo (S/N)? ")
    if nJogo != "s":
        print("Obrigado por jogar. Tchau!")
        break
