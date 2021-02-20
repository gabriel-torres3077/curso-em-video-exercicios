"""
A confederação
nacional de natação
precisa de um
programa que leia
o ano de nascimento de
um atleta e mostre
sua categoria, de
acordo com a idade:

-até 9 anos: MIRIM
-até 14 anos: INFANTIL
-até 19 anos: JUNIOR
-até 20 anos: SÊNIOR
-acima: MASTER
"""
year = int(input('Data de nascimento do atleta: '))
age = 2021 - year
if (age <= 9):
    category = 'Mirim'
elif (age <= 14):
    category = 'Infantil'
elif (age <= 19):
    category = 'Junior'
elif (age <= 20):
    category = 'Sênior'
else:
    category: 'Master'
print('O atleta se enquadra na categoria {]'.format(category))