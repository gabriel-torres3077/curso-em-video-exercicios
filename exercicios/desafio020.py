"""
O mesmo professor
do desafio anterior
quer sortear a ordem
de apresentação de
trabalhos dos alunos.
Faça um programa que
leia o nome dos quatro
alunos e mostre a
ordem sorteada.
"""
from random import shuffle
students = []
for x in range(1,5):
    students.append(input('Ensira o nome do {}º grupo'.format(x)))
shuffle(students)
print(students)
