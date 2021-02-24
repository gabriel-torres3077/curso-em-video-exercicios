"""
Faça um programa
que jogue par ou impar
com o computador. O
jogo só sera
interrompido quando o
jogador PERDER,
mostrando o total de
vitórias consecutivas
que ele conquistou no
final do jogo
"""
from random import randint
computerPick = userPick = userSide = count = 0
while True:
    userSide = str(input('Você escolhe par ou impár ? [P/I] \n>>>'))
    computerPick = randint(0, 100)
    userPick = int(input('Jogue um numero aleatório possitivo \n>>>'))
    result = userPick + computerPick
    if result % 2 == 0 and userSide in 'Pp':
        count+=1
    elif result % 2 == 0 and userSide in 'Ii':
        break
    elif result % 2 != 0 and userSide in 'Pp':
        break
    else:
        print('Escolha ou valor inválidos, por favor tente novamente!')
print('Você venceu {} consecutivas, parabens'.format(count))