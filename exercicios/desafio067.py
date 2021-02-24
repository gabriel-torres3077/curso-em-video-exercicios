"""
Faça um programa
que mostre a tabuada
de vários números, um
de cada vez, para cada
valor digitado pelo
usuário. O programa
será interrompido
quando o número
solicitado for
negativo.
"""
num = 0
while True:
    num = int(input('Ensira o numero para gerar uma tabuada: '))
    if num < 0:
        break
    for x in range(1, 11):
        print('{} x {} = {}'.format(num, x, num * x))
print('Processo finalizado, numero negativo inserido!')