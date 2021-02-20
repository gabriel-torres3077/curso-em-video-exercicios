"""
Desenvolva um programa
que leia o comprimento
de três retas e diga se elas podem ou não formar um triangulo
"""
a = int(input('ensira o comprimento da primeira reta: '))
b = int(input('ensira o comprimento da segunda reta: '))
c = int(input('ensira o comprimento da terceura reta: '))

if(a < b + c and b < a + c and c < a + b):
    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')