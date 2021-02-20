"""
Faça um programa
que leia a largura e a
altura de uma parede
em metros, calcule a
sua área e a
quantidade de tinta
necessária para
pinta-la sabendo que
cada litro de tinta
pinta uma area de 2m²
"""
import math
bucket = 2
width = float(input('Ensira a largura da parede \n>>>'))
height = float(input('Ensira a altura da parede \n>>>'))
area = width * height
print('Largura = {} \nAltura = {} \nArea = {} \nQuantidade de baldes = {}' .format(width, height, area, math.ceil(area / bucket)))
