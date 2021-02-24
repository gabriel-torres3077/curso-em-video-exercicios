"""
Crie um programa
que leia vários
números inteiros pelo
teclado. No final da
execução, mostre a
média entre todos os
valores e qual foi o
maior e o menor
dos valores lidos. o
programa deve perguntar
ao usuário se ele quer ou
não continuar a digitar
valores
"""
from random import randint
count = 1
biggest = 0
smallest = 999
num = randint(5, 10)
values = 0
running = True
average = 0
while running == True:
    values = int(input('Ensira o {} valor: '.format(count)))
    count += 1
    num -= 1
    average += values
    if values > biggest:
        biggest = values
    elif values < smallest:
        smallest = values
    if num == 1:
        num = (int(input('Voce deseja continuar? \n'
                         '[1] para continuar\n'
                          '[0] para finalizar\n>>>'))) * randint(5, 10)
    if num == 0:
        running = False
print('média: {:.2f}\n'
      'menor valor: {} \n'
      'maior valor: {}'.format(average/count-1, smallest, biggest))



