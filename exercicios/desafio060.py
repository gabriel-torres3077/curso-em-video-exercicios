"""
Faça um programa
que leia um número
qualquer e mostre o
seu fatorial
"""
value = int(input('Ensira o valor: '))
result = 1
while value > 0:
    result *= value
    value -= 1
print(result)