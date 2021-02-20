"""
Faça um programa
que leia um ano
qualquer e mostre se
ele é 'BISSEXTO'
"""
year = int(input('Ensira o ano: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('é um ano BISSEXTO')
else:
    print('Não é um ano BISSEXTO')