"""Crie um programa
que leia o nome
completo de uma
pessoa e mostre:
-O nome com todas as letras maiusculas

-O nome com todas as letras minusculas

-Quantas letras ao todo(sem considerar espaços)

-Quantas letras tem o primeiro nome
"""
name = input('Ensira seu nome completo: ')
slipList = name.split()

print('-O nome com todas as letras maiusculas: {}\n'
      '-O nome com todas as letras minusculas: {}\n'
      '-Quantas letras ao todo(sem considerar espaços): {}\n'
      '-Quantas letras tem o primeiro nome: {}' .format(name.upper(), name.lower(), len(name), len(slipList[0])))