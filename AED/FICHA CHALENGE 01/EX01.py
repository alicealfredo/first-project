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