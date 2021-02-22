"""
Desenvolva um
programa que leia o
nome, idade e sexo de
4 pessoas. No final do
programa mostre:

-A média de idade do grupo
-Qual é o nome do homem mais velho
-Quantas mulheres tem menos de 20 anos
"""
averageAge = 0
women= 0
OldestManAge = 0
OldestManName = ''
for people in range(1, 5):
    name = input('Nome: ')
    age = int(input('Idade: '))
    sex = (input('Sexo: '))
    averageAge += age
    if sex in 'Ff' and age >= 20:
        women += 1
    if age >= OldestManAge and sex in 'Mm':
        OldestManAge = age
        OldestManName = name


print(averageAge/4)
print(name)
print('Média de idade do grupo: {} \n'
      'Nome do homem mais velho: {} com {} anos \n'
      'Mulheres com menos de 20 anos: {}' .format(averageAge/4, OldestManName, OldestManAge, women))