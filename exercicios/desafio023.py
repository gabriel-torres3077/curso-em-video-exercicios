"""
Faça um programa
que leia um número de
0 a 9999 e mostre na
tela cada um dos dígitos separados.
"""
num = input('Ensira um valor de 0 a 9999: ')
print('Unidade: {} \nDezena: {} \nCentena: {} \n Milhar: {}'.format(num[3], num[2], num[1], num[0]))