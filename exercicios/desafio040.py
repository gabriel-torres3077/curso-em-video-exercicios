"""
Crie um programa
que leia duas notas de
um aluno e calcule sua
média, mostrando uma
mensagem no final, de
acordo com a média
atingida:

-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO
"""
grade = float(input('Nota do aluno: '))
if (grade < 5.0):
    print('REPROVADO!')
elif(grade>=5 and grade < 7):
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')