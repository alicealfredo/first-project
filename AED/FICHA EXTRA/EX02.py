"""Create a function called square(number).
This function aims to print a square of *, as shown in the image.
The function's input parameter represents the number of lines of the square to
print.
"""

def square(number):
    for i in range(0,number):
        print(" * "*number)

square(7)