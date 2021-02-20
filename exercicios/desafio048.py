"""
Faça um programa
que calcule a soma entre
todos os numeros ímpares que
são multiplos de tres e
que se encontram no intervalo de 1 até 500.
"""
count = 0
for x in range(1, 501):
    if (x % 3 ==0 and x % 2 !=0):
       count += x
print(count)