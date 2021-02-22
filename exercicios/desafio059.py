"""
Crie um programa
que leia dois valores e
mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa

Seu programa deverá
realizar a operação
solicitada em cada caso
"""
num1 = int(input('Ensira o valor 1: '))
num2 = int(input('Ensira o valor 2: '))
close = False
while close == False:
    action = int(input('\n[1] Somar \n'
                       '[2] Multiplicar \n'
                       '[3] Maior\n'
                       '[4] Novos Números\n'
                       '[5] Sair do programa\n>>>'))
    if action == 1:
        print(num1 + num2)
    elif action == 2:
        print(num1 * num2)
    elif action == 3:
        if num1 > num2:
            print(num1)
        elif num2 > num1:
            print(num2)
        else:
            print('Os valores são iguais')
    elif action == 4:
        num1 = int(input('Digite o novo primeiro valor: '))
        num2 = int(input('Digite o novo segundo valor: '))
    elif action == 5:
        close == True
        break
    else:
        print('Escolha inválida tente novamente')