"""
Fala um programa
que leia três numeros
e mostre qual é o maior
e qual é o menor.
"""
num = []
for x in range(1,4):
    num.append(int(input('Ensira os valores: ')))
print('Dos 3 valores indicados o menor número é {} e o maior é {}'.format(num[0], num[2]))
