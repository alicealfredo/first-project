"""Create a seconds to hours/minutes/seconds converter!
You should ask the user to indicate a certain number of seconds.
Then convert this seconds value into the corresponding number of hours,
minutes, and seconds, as illustrated in the following examples:
7300 seconds = 2 hours, 1 minutes, 40 seconds
8054 seconds = 2 hours, 14 minutes, 14 seconds
"""

tempo = int(input('Indique o tempo em segundos: '))
horas=tempo/3600
minutos=(tempo%3600)/60
segundos=tempo%60

print(f"{horas:.0f} horas, {minutos:.0f} minutos, {segundos:.0f} segundos")