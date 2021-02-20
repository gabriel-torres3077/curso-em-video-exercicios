"""
Crie um programa
que leia o nome de uma
cidade e diga se ela
começa ou não com o nome "santo"
"""
city = str(input('Escreva o nome da cidade: ')).strip()
print(city[:5].upper() == 'SANTO')
