"""
Refaça o desafio 035
dos triangulos acrescentando
o recurso de mostrar o tipo de
triangulo será formado:

-Equilatero: todos os lados iguals
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes
"""
a = int(input('ensira o comprimento da primeira reta: '))
b = int(input('ensira o comprimento da segunda reta: '))
c = int(input('ensira o comprimento da terceura reta: '))

if(a < b + c and b < a + c and c < a + b):
    if(a == b and b == c):
        type = 'Equilátero'
    elif (a == b or b == c or a == c):
        type = 'Isósceles'
    elif (a != b and b != c and a != c):
        type = 'Escaleno'
    print('É possivel formar um triangulo do tipo {}' .format(type))
else:
    print('Não é possivel gerar um triangulo')