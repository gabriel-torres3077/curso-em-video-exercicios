"""
Escreva um programa que
pergunte a quantidade de
KM percorridos por um carro
alugado e a quantidade de dias
pelos quais ele foi alugado.
Calcule o preço a pagar.
Sabendo que o carro custa R$60
por dia e R$0,15 por KM rodado
"""
km = float(input('Ensira quantos KM foram percorridos: '))
days = int(input('Ensira quantos dias o cliente permaneceu com o carro: '))
total = (km * 0.15) + (days * 60)
print('A preço a ser pago é : {:.2f}R$'.format(total))