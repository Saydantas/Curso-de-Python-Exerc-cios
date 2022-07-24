'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule
e mostre o comprimento da hipotenusa.'''

from math import hypot
co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))
hi = hypot(co, ca)
print(f'De acordo com as medidas fornecidas a hipotenusa tem {hi:.2f}')
