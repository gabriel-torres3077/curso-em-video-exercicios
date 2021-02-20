""""
Faça um programa
que leia um numero
inteiro e mostre na
tela a sua tabuada
"""

n = int(input('Ensira um numero inteiro: '))
for x in range(1, 11):
    print('{} X {} = {}'.format(n, x, x*n))