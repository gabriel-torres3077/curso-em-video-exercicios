"""
Escreva um
programa que
pergunte o salário de
um funcionário e
calcule o valor do seu aumento.

Para salários
superiores a
R$1.250,00 calcule um
aumento de 10%

Para os inferiores ou
iguais, o aumento é de
15%
"""
wage = float(input('Ensira o valor do salário: '))
if (wage <= 1250.00):
    increase = 0.1
    newWage = wage + (wage * increase)
else:
    increase = 0.15
    newWage = wage + (wage * increase)
print('Salário antigo: {} \n'
      'Aumento: {}% \n'
      'Novo salário: {}' .format(wage, increase * 100, newWage))