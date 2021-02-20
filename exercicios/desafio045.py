"""
Crie um programa que faça
o computador jogar jokenpô com você
"""
from random import randint
playerTry = int(input('Escolha um: \n'
                      '1 - pedra \n'
                      '2 - papel \n'
                      '3 - tesoura \n'
                      '>>>'))
computerTry = int(randint(1,3))
simbols = ['Pedra', 'Papel', 'Tesoura']
print('Escola do computador: {} \n'
      'Sua escolha: {}' .format(simbols[computerTry-1], simbols[playerTry-1]))
if(playerTry == 1):
    if (computerTry == 1):
        print('Vocês empataram!!')
    elif(computerTry == 2):
        print('Você perdeu!!!')
    elif(computerTry == 3):
        print('Você venceu !!!!')
    else:
        print('Jogada inválida')
if(playerTry == 2):
    if (computerTry == 2):
        print('Vocês empataram!!')
    elif(computerTry == 3):
        print('Você perdeu!!!')
    elif(computerTry == 1):
        print('Você venceu !!!!')
    else:
        print('Jogada inválida')
if(playerTry == 3):
    if (computerTry == 3):
        print('Vocês empataram!!')
    elif(computerTry == 1):
        print('Você perdeu!!!')
    elif(computerTry == 2):
        print('Você venceu !!!!')
    else:
        print('Jogada inválida')