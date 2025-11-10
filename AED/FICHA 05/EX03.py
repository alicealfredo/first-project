"""
3. Develop a program that allows you to manage a small parking car with 3 rows, each one with
5 parking places. The park layout is similar to that shown in the image:
When the program starts, all parking places must be free. Your program should start through
a menu with the following options:
MENU
1 - Car Entrance
2 - Car Exit
3 - Park State
0 - Exit

• Car Entrance: must occupy the first parking place that is free, starting from row 1 (place
1) and ending in row 3 (place 5). You must indicate on the console the position of the
seat to be occupied.
If all parking seats are occupied, please show the message "Park Complete!".
• Car Exit: The user must indicate the position of their car in the car park: row and place. The
indicated position must be occupied, changing its status to free.
• Park Status: this option should show the park's occupancy. It should show the number
of occupied places and the number of free places in the park.
"""
def carEntrance(filas):
    for i in range(len(filas)):
        for j in range(len(filas[i])):
            freePos = filas[i].index("free")
            del filas[i][freePos]
            filas[i].insert(freePos,"in use")
            break
        break

    print(f"\nLugar ocupado - Row: {i+1}")
    print(f"Place: {freePos+1}")
    return filas

def carExit(filas):
    row = int(input("Row: "))
    place = int(input("Place: "))
    for i in range(len(filas)):
        for j in range(len(filas[i])):
            del filas[row-1][place-1]
            filas[row-1].insert(place-1,"free")
            break

filas = [["free","free","free","free","free"],
         ["free","free","free","free","free"],
         ["free","free","free","free","free"]
         ]

option = 4
while option != 0:
    print("\tMENU")
    print("1 - Car Entrance")
    print("2 - Car Exit")
    print("3 - Park State")
    print("0 - Exit")
    option = int(input("\nChoose one of the options: "))

    if option == 1:
        carEntrance(filas)
    elif option == 2:
        carExit(filas)
    elif option == 3:
        print("Free places:")
        print(f"Rows: {filas.count('free')}")
        print(f"Places: {filas.count('free')}")
        
    elif option == 0:
        break
    else:
        print("Choose a valid option")


