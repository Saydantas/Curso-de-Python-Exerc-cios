'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

n = int(input('Digite um número para saber se é PAR ou ÍMPAR: '))
if n % 2 == 0:
    print(f'O número {n} é PAR.')
else:
    print(f'O número {n} é ÍMPAR.')
