"""
Faça um programa
que leia o peso de
cinco pessoas. No
final mostre qual foi o
maior e o menor peso
lidos.
"""
group = []
people = 0
for people in range(1, 6):
    group.append(float(input('Ensira o peso do {}º candidato: '.format(people))))
group.sort()
print('Maior peso: {:.2f} KG \n'
      'Menor peso: {:.2f} KG'.format(group[0], group[4]))
