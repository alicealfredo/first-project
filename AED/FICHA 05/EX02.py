"""
1. Implement a program that allows you to record and analyze rainfall indices in four cities
(Braga, Porto, Lisbon) over 6 months (from January to June).
    1.1 Create a two-dimensional list called rainfall, where:
        • Each line represents a city;
        • Each column represents a month.
    1.2 Your application should:
            • Ask the user to indicate the rainfall values (in millimeters of rain). If you prefer, you
            can generate the monthly rainfall values for each city, randomly between 0 and 100;
            • Show the data you enter, in table format;
            • Call a function named dataAnalysis(rainfall) that calculates and returns:
                - o The average rainfall of each city over the 6 months;
                - o The average rainfall for each month (considering all cities);
                - o The highest and lowest rainfall recorded and in which city and month it occurred.
"""
def showData(rainfall):
    for i in range(len(rainfall)):
        for j in range(len(rainfall[i])):
            print(rainfall[i][j], end = "\t")
        print("\n")

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
cidades =["Braga", "Porto", "Lisboa"]
rainfall = []

ncidades = 4
nmeses = 6

for i in range(ncidades):
    print(f"Pluviosidade em {cidades[i]}")
    rainfall.append([])
    for j in range(nmeses):
        value = int(input(f"{meses[j]} : "))
        rainfall[i].append(value)
    print("\n")

showData(rainfall)
