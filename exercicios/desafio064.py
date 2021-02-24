"""
Crie um programa
que leia vários
números inteiros pelo
teclaso. O programa só
vai parar quando o
usuário digitar o valor
999, que é a condição
de parada. No final,
mostre quantos números
foram digitados e qual
foi a soma entre eles
"""
num = 0
count = 0
sum = 0
while num != 999:
    count += 1
    sum += num
    num = int(input('Ensira o valor para ser adicionado: '))

print('Foram digitados: {} numeros e a soma de todos foi: {}'.format(count-1, sum))