"""
Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente
de um triangulo retangulo, calcule e
mostre o comprimento da hipotenusa
"""
catetoAd = float(input('Cateto Adjacente: '))
catetoOp = float(input('Cateto Oposto: '))
hipotenusa = (catetoAd ** 2) + (catetoOp ** 2)
print('Hipotenusa: {}'.format(hipotenusa))