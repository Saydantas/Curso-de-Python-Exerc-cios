'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc
n = float(input('Digite um número para obter sua porção inteira: '))
print(f'O número {n} tem a parte inteira {trunc(n)}')
