"""
Desenvolva uma
lógica que leia o peso e
a altura de um
pressoa, calcule seu
IMC e mostre seu status,
de acordo com a tabela abaixo:

-abaixo de 18.5: abaixo do peso
-entre 18.5 e 25: peso ideal
-25 até 30: sobrepeso
-30 até 40: obesidade
-acima de 40: obesidade móbida
"""
height = float(input('Ensira a altura em metros: '))
weight = float(input('Ensira o peso em kg: '))
imc = weight / (height * height)
if(imc < 18.5):
    status = 'Abaixo do peso'
elif (imc <= 25):
    status = 'Peso ideal'
elif (imc <= 30):
    status = 'Sobrepeso'
elif (imc <= 40):
    status = 'Obesidade'
else:
    status = 'obesidade mórbida'
print('Uma pessoa com {} de altura e pesando {} está classificada como: {}' .format(height, weight, status))