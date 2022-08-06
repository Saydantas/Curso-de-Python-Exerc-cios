'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
ou perdeu.'''

from random import randint
from time import sleep
cpu = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número pensei? '))
print('Processando...')
sleep(1)
if n == cpu:
    print(f'Parabéns! você acertou, pensei no {cpu} também.')
else:
    print(f'Que pena, você errou pensei no {cpu}')
