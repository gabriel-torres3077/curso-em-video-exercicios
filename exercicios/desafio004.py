"""
Faça um programa
que leia algo pelo
teclado e mostre na
tela o seu tipo
primitivo e todas as
informações possiveis
sobre ele
"""
x = input('Ensira qualquer dado: ')
print('Data Type: {} \nIs numeric?: {} \nIs decimal?: {}'.format(type(x), x.isnumeric(), x.isdecimal()))