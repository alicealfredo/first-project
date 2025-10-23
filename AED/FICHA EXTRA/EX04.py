"""Create a function called geometricDiamond(number).
This function aims to print a geometric diamond shape of *, as shown in the im-
age.
The function's input parameter represents the height of the diamond from its
largest base to the top.
"""

def geometricDiamond(number):
    for i in range(0,number):
        contador = 0
        contador2 = number+1
        while contador <= number:
            contador += 1
            parte1 = (" "*(number-(contador-1))) + (" *"*contador)
            print(parte1)
            continue
        else:
            for i in range(number,number*2):
                contador2 -= 1
                parte2 = (" "*(number-(contador2-1))) + (" *"*contador2)
                print(parte2)
            break

geometricDiamond(7)