"""
Crie um programa
que leia quanto
dinheiro uma pessoa
tem na carteira e
mostre quantos
dólares ela pode
comprar
"""

# conversão US$1,00 = R$3,27

c_rate = 3.27
currency = int(input('Quanto dinheiro você tem atualmente? \n>>> '))
print(currency*c_rate)