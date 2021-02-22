"""
Faça um programa
que leia o sexo de uma
pessoa, nas só aceite
os valores 'M' ou 'F'
Caso esteja errado peça
a digitação novamente até
ter um valor correto.
"""

sex = str(input('Ensira o sexo: '))
while sex not in 'MF':
    sex = input('Ensira um valor válido: ')
