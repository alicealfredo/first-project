"""Implement the invertText(text) function. The function should receive a
text (string), based on an input, and should print the same text but in
reverse order.
"""

def invertText(text):
    for i in range(len(text)-1,-1,-1):
        print(text[i],end="")

text = str(input('Indique um texto: '))
invertText(text)