"""
Crie um programa
que simule o
funcionamento de um
caixa eletronico. No
início, pergunte ao
usuário qual será o
valor a ser sacado
(número inteiro) e o
programa vai informar
quantas cédulas de
cada valor serão
entregues

Obs: considere que o
caixa possui cédulas
de R$50, R$20, R$10 e
R$1.
"""
withdraw = value = 0
value = int(input('Quanto você deseja sacar? \n>>>'))
total = value
ced = 50
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        print(f'total de {totalCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break



