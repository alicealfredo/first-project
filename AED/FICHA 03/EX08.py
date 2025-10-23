"""Write the function reverseWords(text) that receives a text and returns
the same text, but with the words in reverse order.
"""

def reverseWords(text):
    palavras = text.split()
    invertido = palavras[::-1] 
    resultado = " ".join(invertido) #transforma a lista em uma string
    return resultado

text = str(input("Texto: "))
print(reverseWords(text))