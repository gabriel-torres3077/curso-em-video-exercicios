"""
Crie um programa
que leia o nome e o
preço de vários
produtos. O programa
severá perguntar se o
usuário vai continuar.
No final, mostre:
-Qual é o total gasto na compra
-Quantos produtos custam mais de R$ 1000
-Qual é o nome do produto mais barato.
"""
cheapestPrice = 9999999
productPrice = total = count =0
cheapestName = productName = keepRegister = ''
while True:
    productName = str(input('Ensira o nome do produto: '))
    productPrice = float(input('Ensira o preço do produto: '))
    total += productPrice
    if productPrice < cheapestPrice:
        cheapestName = productName
        cheapestPrice = productPrice
    if productPrice > 1000:
        count += 1
    keepRegister = str(input('Você deseja continuar cadastrando os produtos? [S/N]: '))
    if keepRegister in 'Nn':
        break

print('-Qual é o total gasto na compra: {:.2f}\n'
        '-Quantos produtos custam mais de R$ 1000: {}\n'
        '-Qual é o nome do produto mais barato: {}'.format(total, count, cheapestName))