"""
Faça um programa
que leia um número
inteiro e diga se ele é
ou não um numero primo
"""
num = int(input('Ensira um numero inteiro: '))
prime = False
for x in range(2, num):
    if(num % x == 0):
        prime = False
        break
    else:
        prime = True
print('{} é um numero primo? {}' .format(num, prime))
