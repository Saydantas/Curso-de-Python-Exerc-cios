'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan,radians
n = float(input('Digite o angulo: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print(f'Seu seno é {s:.2f}, seu cosseno é {c:.2f} e a tangente é {t:.2f}')
