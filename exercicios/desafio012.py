"""
Faça um algoritmo
que leia o preço de um
produto e mostre seu
novo preço, com 5% de
desconto.
"""
desconto = 0.05
price = float(input('Ensira o valor do produto: '))
print('valor do produto: {} \n'
      'Desconto: {} \n'
      'valor com desconto: {}' .format(price, desconto, price-(price*desconto)))