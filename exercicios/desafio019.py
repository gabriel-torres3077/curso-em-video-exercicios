"""
Um professor quer
sortear um dos seus
quatro alunos para
apagar o quadro. Faça
um programa que ajude
ele, lendo o nome deles
e escrevendo o nome escolhido
"""
from random import randint
students = [ ]
for x in range(1,5):
    students.append(input('Ensira o nome do {}º aluno'.format(x)))
print(students[randint(1,4)])