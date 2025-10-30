"""
Develop a program that allows you to input a company's monthly sales over the 12 months
of the year (from January to December). After that, the program should include the call of 3
functions which they return, respectively:
• the month with the highest value of sales;
• the month with the lowest value of sales;
• The average monthly sales.
"""
def maiorvendas():
    maiorVendas = max(faturacao)
    mesMaiorVendas = faturacao.index(maiorVendas)
    return mesMaiorVendas, meses[mesMaiorVendas]
def menorvendas():
    menorVendas = min(faturacao)
    mesMenorVendas = faturacao.index(menorVendas)
    return mesMenorVendas, meses[mesMenorVendas]
def mediaVendas():
    soma = sum(faturacao)
    media = soma / len(faturacao)
    return media

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
i = 0
faturacao = []
while i < 12:
    vendasMes =int(input(f"Indique a faturação do mês de {meses[i]}: "))
    i += 1
    faturacao.append(vendasMes)

mesMaiorVendas, meses[mesMaiorVendas] = maiorvendas()
mesMenorVendas, meses[mesMenorVendas] = menorvendas()
media = mediaVendas()
print(f"Mês de maior faturação é: {meses[mesMaiorVendas]}")
print(f"Mês de menor faturação é: {meses[mesMenorVendas]}")
print(f"Média de faturação é: {media}")