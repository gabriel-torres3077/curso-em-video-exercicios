"""
Elabore um programa
que calcule o valor a ser
pago por um produto
considerando o seu
preço normal e condição
de pagamento:

-á vista dinheiro/cheque: 10% de desconto
-á vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
"""
productValue = float(input('valor original do produto: '))
paymentMethod = int(input('Qual será o metodo de pagamento? \n'
                          '1 - para dinheiro / cheque \n'
                          '2 - para cartão'))
if (paymentMethod == 1):
    finalValue = productValue - (productValue * 0.1)
elif (paymentMethod == 2):
    installments = int(input('Em quantas parcelas será pago? '))
    if (installments == 1):
        finalValue = productValue - (productValue * 0.05)
    elif (installments == 2):
        finalValue = productValue
    elif(installments >= 3):
        finalValue = productValue + (productValue * 0.2)
    else:
        print('Qualtidade de parcelas inválidas por favor ensira um valor válido!')
else:
    print('Método de pagamento inválido por favor tente novamente!')
print('valor inicial do produto: R${:.2f} \n'
      'Valor final do produto: R${:.2f}' .format(productValue, finalValue))
