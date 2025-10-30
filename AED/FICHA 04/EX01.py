"""
Implement a program to help a teacher to analyze the grades of their students.
Program requirements:
• Read student grades from user input and store them in a list. The student’s grades must
be between [0-20] in float format (input validated with exceptions). The user should
enter the grades of 10 students.
• After all grades have been entered, the program should call the function named data-
Grades (list). The function receives the list of grades and should return:
The highest and lowest grades.
How many grades are above av-
erage?
"""
def dataGrades(grades):
    grades = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
    notaMax = grades[0]
    notaMin = grades[0]
    soma = 0
    acimaMedia = 0
    for i in range(len(grades)):
        if grades[i] > media:
            acimaMedia += 1
        else:
            if grades[i] > notaMax:
                notaMax = grades[i]
                soma += grades[i]
            elif grades[i] < notaMin:
                notaMin = grades[i]
            media = soma / len(grades)
    return notaMax, notaMin, acimaMedia

try:
    n1 = float(input("1ª Avaliação: "))
    n2 = float(input("2ª Avaliação: "))
    n3 = float(input("3ª Avaliação: "))
    n4 = float(input("4ª Avaliação: "))
    n5 = float(input("5ª Avaliação: "))
    n6 = float(input("6ª Avaliação: "))
    n7 = float(input("7ª Avaliação: "))
    n8 = float(input("8ª Avaliação: "))
    n9 = float(input("9ª Avaliação: "))
    n10 = float(input("10ª Avaliação: "))
    grades = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
    for i in range(len(grades)):
        if grades[i] < 0 or grades[i] > 20:
            raise ValueError()
    dataGrades(grades)
    notaMax, notaMin, acimaMedia = dataGrades(grades)
    print(f"Maior nota: {notaMax}")
    print(f"Menor nota: {notaMin}")
    print(acimaMedia)
    
except ValueError:
    print("Valor inválido. Insira uma nota entre 0 e 20.")
except:
    print("Valor inválido. Insira uma nota válida.")