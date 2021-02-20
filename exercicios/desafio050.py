"""
Desenvolva um programa que leia
seis numeros inteiro e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for
impar desconsidere-o
"""
s = 0
for x in range(1, 7):
    num = int(input('Ensira o valor desejado: '))
    if (num % 2 == 0):
        s += num
print(s)