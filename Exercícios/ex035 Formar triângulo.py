'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
não formar um triângulo.'''

n1 = int(input('Digite o tamanho da primeira reta: '))
n2 = int(input('Digite o tamanho da segunda reta: '))
n3 = int(input('Digite o tamanho da terceira reta: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('Essas medidas podem formar um triângulo.')
else:
    print('Essas medidas NÃO podem formar um triângulo.')
