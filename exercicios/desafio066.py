"""
Crie um programa
que leia vários
números inteiros pelo
teclado. O programa só
vai parar quando o
usuário digitar o valor
999, que é a condição
de parada. No final mostre
quantos números foram
digitados e qual foi a
soma entre eles
"""
sum = count = value = 0
while True:
    value = int(input('Ensira o valor {}: '.format(count+1)))
    if value == 999:
        break
    sum += value
    count+=1
print('Quantidade de valores: \n'
      'Soma de todos os valores: '.format(count, sum))
