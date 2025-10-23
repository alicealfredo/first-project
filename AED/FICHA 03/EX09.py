"""Implement the function printCharLine(text,numberChar) that receives two
arguments: a text, and the number of characters you want to print per
line.
Your function should print the text based on this number of characters,
as shown in the image below.
"""

def printCharLine(text,numberChar):
    contador = 0 
    for i in range(0, len(text), numberChar):
        print(text[i:i+numberChar])

text = str(input("Texto: "))
numberChar = int(input("Nº caracteres a imprimir por linha: "))

printCharLine(text,numberChar)