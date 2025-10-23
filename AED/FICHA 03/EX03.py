"""Create the function capicua(text) that receives a text as an input param-
eter and returns True or False, depending on whether the text is a capicua
or not.
A capicua or palindrome word consists on text that can be read from left
to right as from right to left.
Examples of palindromes words: osso, asa, ana, arara
Examples of the usage of capicua function:
capicua('osso') => returns True
capicua('roma') => returns False
Depending on the value returned by the function (True or False), you
should print in the console application if the word is capicua or not.
"""

def capicua(text):
    if text == text[::-1]: # text[::-1] - inverter o texto
        return True
    else:
        return False

text = str(input('Indique um texto: ')).lower()
if capicua(text)==True:
    print(f"{text} é uma capicua")
else:
    print(f"{text} não é uma capicua")