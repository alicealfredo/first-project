"""1. Create a function called triangle(number).
This function should print a triangle of *. The height of the triangle (Nº
lines) depends on the function's input parameter, which represents the height of
the triangle to be printed.
"""

def triangle(number):
    for i in range(0,number):
        contador = 0
        espacos = number
        while contador <= number:
            contador += 1
            final = (" "*(espacos-(contador-1))) + (" *"*contador) 
            print(final)
        break

triangle(7)