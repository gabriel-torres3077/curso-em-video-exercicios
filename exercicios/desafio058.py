"""
Melhore o jogo do
DESAFIO 028 onde o
computador vai
"pensar" em um
número entre 0 e 10 . Só
que agora o jogador vai
tentar adivinhar até
acertar, mostrando no
final quantos palpites
foram necessários para vencer.
"""
from random import randint
computerInt = randint(1, 10)
userInput = int(input('Tente adivinhar o número! \n>>>'))
userTies = 0
while userInput != computerInt:
    userInput = int(input('Você errou tente novamente \n>>>'))
    userTies += 1
print('Parabens você acertou!!!!\n'
      'Foram necessárias {} tentativas' .format(userTies))
