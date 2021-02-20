"""
Refaça o desafio 009, mostrando a tabuada
de um numero que o usuário escolher só que
agora ultilizando um laço for.
"""
num = int(input('Ensira o numero desejado para a visualização da tabuada: '))
for x in range (1, 11):
    print('{} X {} = {}' .format(num, x, num * x))