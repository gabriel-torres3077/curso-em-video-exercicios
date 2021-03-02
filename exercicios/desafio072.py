"""
Crie um programa
que tenha uma tupla
totalmente preenchida
com uma contagem por
extenso de zero até vinte.

Seu programa deverá
ler um número pelo
teclado (entre 0 e 20)
e mostra-lo por extenso
"""
numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
       'Seis', 'Sete', 'Oito','Nove', 'Dez', 'Onze',
       'Doze', 'Treze','Quatorze', 'Quinze', 'Dezeseis',
       'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print(numbers)
num = int(input('Ensira o valor a ser analizado por extenso: '))
while True:
    if num < 20 and num > -1:
        print(numbers[num])
        break
    else:
     num = int(input('Valor incorreto. Ensira o valor a ser analizado por extenso: '))