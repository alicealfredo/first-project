"""Create a function named frameTable(number).
This function aims to print a table of *, as shown in the image.
The function's input parameters represent the number of rows and columns of the
table to be printed.
"""

def frameTable(lin: int, col: int):
    print("* "*col)
    for i in range(1,lin-1):
        print("*"," "*(col+2),"*")
    print("* "*col)

frameTable(5,7)