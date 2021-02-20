"""
Desenvolva um
programa que
pergunte a distância
de uma viagem em km.
calcule o preço da
passagem, cobrando
R$0,50 por km para
viagens de até 200km
e R$0,45 para viagens
mais longas.
"""
distance = float(input('Ensira a distância da viagem: '))
if (distance > 200):
    price = 0.5
else:
    price = 0.45
print('O valor da passagem é: {:.2f}' .format(distance * price))