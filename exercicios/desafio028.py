"""
Escreva um
program que fala o computador
'pensar' em um numero inteiro
entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número
escolhido pelo computador.

o programa deverá escrever na tela
se o usuário venceu ou perdeu

obs: usando apenas 'if'
"""
import random
tries = 3
answer = random.randint(1,5)
while (tries > 0):
    guess = int(input('Tente adivinhar o numero: '))
    if(guess == answer):
        print('Parabens você acertou e ultilizou {} tentativa(s)' .format(tries))
    else:
        print('Você errou tente novamente\n')
        tries-=1

#resolução seguindo o desafio:
"""
import random
answer = random.randint(1,5)
guess = int(input('Tente acertar o numero: '))
if (guess == answer):
    print('Parabens você acertou')
else:
    print('você errou reinicie e tente novamente')
"""