"""
Faça um programa
que leia o nome
completo de uma
pessoa. mostrando em
seguida o primeiro e o
ultimo nome separadamente
"""
name = input('Digite seu nome completo: ')
splittedName = name.split()
print('Primeiro nome: {}\n'
      'Ultimo Nome: {}' .format(splittedName[0], splittedName[-1]))