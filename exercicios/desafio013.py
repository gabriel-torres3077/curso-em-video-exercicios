"""
Faça um algoristmo
que leia o salário de um
funcionário e mostre
seu novo salário com
15% de aumento
"""
increase = 0.15
wage = float(input('>>>Ensira o valor do salario: \n>>>'))
print('Salario: {} \n'
      'acescimo: 15%\n'
      'salário final: {}'.format(wage, wage+(wage*increase)))

