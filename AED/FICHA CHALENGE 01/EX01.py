"""A security company has developed a digital safe (cofre digital) that only opens when the user
enters a secret sequence of numbers, in the correct order.
1. The safe has a password made up of 4 integers, each one of them between 0 and 9 (e.g.,
3, 1, 4, 1). Generate the secret password randomly.
2. Implement a function openSafe() that simulates how this digital safe works following
these rules:
2.1. The user can try to guess the password by entering 4 numbers per attempt.
2.2. After each attempt, the program must display:
• The numbers that are correct, in the right positions.
• Or message that no number is correct (in each position)
2.3. The game ends when the user guesses the full sequence or after 10 attempts.
At the end, the program should display a victory or failure message.
"""
import random

# Função que recebe a tentativa do utilizador e verifica se há algum dígito na posição correta
def openSafe():
    correctPositions = 0
    for i in range(4):
        if userGuess[i] == password[i]:
            correctPositions += 1
    return correctPositions

# Senha aleatória de 4 dígitos
i = 0
password = []
while i < 4:
    n = random.randint(0, 9)
    i += 1
    password.append(n)

# Imprimir mensagem inicial
print("\n\t\t\t=== DIGITAL SAFE ===\t\t\t")
print("\tTry to guess the SECRET CODE (4 numbers between 0 to 9)\t")
print("\t\t\tYou have 10 attempts.\t\t\t\n")

# Tentativas do utilizador para adivinhar a senha
for t in range(10):
    userInput = input(f"Attempt {t+1} - Enter your 4 numbers separated by spaces: ")
    userGuess = []
    for car in userInput.split():
        userGuess.append(int(car))

    correctPositions = openSafe()

    # Imprime ao utilizador se há números corretos em cada posição
    if correctPositions == 4:
        print("Congratulations! The password is correct.")
        break
    elif correctPositions > 0:
        print(f"→ {correctPositions} correct and in the right position.")
    else:
        print("→ No number is correct in the right position.")


if correctPositions == 4:
    print("VICTORY")
else:
    print("FAILURE")