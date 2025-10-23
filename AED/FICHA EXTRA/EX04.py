"""Create a function called geometricDiamond(number).
This function aims to print a geometric diamond shape of *, as shown in the im-
age.
The function's input parameter represents the height of the diamond from its
largest base to the top.
"""

def geometricDiamond(number):
    for i in range(0,number*2):
        contador = 0
        while contador <= number:
            contador += 1
            final1 = (" "*(number-(contador-1))) + (" *"*contador)
            print(final1)
        break

geometricDiamond(7)