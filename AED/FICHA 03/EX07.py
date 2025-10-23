"""Implement the generatePassword(userName) function that works as a pass-
word generator: the function must receive a username, and based on that
name it must generate and return a password which is generated as follows:
• The password consists of the characters from the even positions of
the username, interspersed by a random number between 1 and 9 (in-
clusive).
• The password ends with the number of characters included in the
username.
• If the userName includes any spaces, the function should return
the message “username is invalid” as an alternative to the pass-
word.
"""
import random

def generatePassword(userName):
    if " " in userName:
        return "Nome de usuário inválido"
    else:
        password = ""
        
        for i in range(1, len(userName), 2): #percorre somente os caracteres pares
            num = random.randint(1, 9)
            password += userName[i] + str(num)
        
        password += str(len(userName))
    
        return password
    
userName = str(input("Username: "))
print("Password:",generatePassword(userName))
