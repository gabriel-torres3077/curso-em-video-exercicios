"""
Escreva um
programa que leia
um numero inteiro
qualauer e peça para o
usuario escolher qual
sera a base de conversão

1 para binário
2 para octal
3 para hexadecimal
"""
num = int(input('Ensira um valor inteiro: '))
conv = int(input('Escolha a base da coversão: \n'
                 '1 - para binário \n'
                 '2 - para octal\n'
                 '3 - para hexadecimal'))
if (conv == 1):
    print('{} para binário: {}' .format(num, bin(num)))
elif (conv == 2):
    print('{} para octal: {}' .format(num, oct(num)))
elif (conv == 3):
    print('{} para hexadecimal: {}'.format(num, hex(num)))
else:
    print('Valor inválido, por favor tente novamente') 
