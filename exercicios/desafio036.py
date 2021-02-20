"""
Escreva um
programa para aprovar
o empéstimo bancário
para a compra de uma
casa. O programa vai
perguntar o valor da casa,
o salário do comprador e em
quantos anos ele vai pagar.

calcule o valor da prestação mensal
sabendo que ela não pode exceder 30%
do salário ou então o emprestimo será negado
"""
houseValue = float(input('Qual o valor da casa? '))
wage = float(input('Qual o salário? '))
years = int(input('Em quantos anos será pago? '))

if ((houseValue / (years * 12))< (wage*0.3)):
    print('empréstimo permitido')
else:
    print('Empréstimo negado!')
