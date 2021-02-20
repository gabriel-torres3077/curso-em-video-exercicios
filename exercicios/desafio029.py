"""
ESCREVA UM PROGRAMA
QUE LEIA A VELOCIDADE DE UM CARRO

se ele ultrapassar 80km/h mostre
uma mensagem dizendo que ele foi multado.

a multa deve custar R$7,00 PARA CADA KM
ACIMA DO LIMITE
"""
speed = float(input('Velocidade do carro: '))
if (speed > 80):
    fine = (speed-80) * 7.00
    print('Você foi multado em {}R$ por estar a {}KM/h em uma via de 80KM/h' .format(fine, speed))