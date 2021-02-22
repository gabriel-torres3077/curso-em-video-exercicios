"""
Crie um programa que
leia o ano de nascimento
de sete pessoas. No final
mostre quantas
pessoas ainda não
atingiram a maioridade
e quantas já são maiores.
"""
adults = 0
children = 0
for x in range(1, 8):
    year = int(input('Ensira o ano de nascimento da {}º pessoa: ' .format(x)))
    age = 2021-year
    if age >= 18:
        adults += 1
    else:
        children += 1
print('Crianças: {}\n'
      'Adultos: {}' .format(children, adults))