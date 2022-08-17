'''Crie um programa que faça o computador jogar Jokenpô com você.'''
cores = {'limpa':'\033[m',  # Modulo com codigos
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[37m'}
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador >=3:
    print('JOGADA INVÁLIDA!')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[cpu]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if cpu == 0:
    if jogador == 0:
        print(f'{cores["amarelo"]}EMPATE{cores["limpa"]}')
    elif jogador == 1:
        print(f'VOCÊ {cores["verde"]}VENCEU{cores["limpa"]}')
    elif jogador ==  2:
        print(f'VOCÊ {cores["vermelho"]}PERDEU{cores["limpa"]}')
elif cpu == 1:
    if jogador == 0:
        print(f'VOCÊ {cores["vermelho"]}PERDEU{cores["limpa"]}')
    elif jogador == 1:
        print(f'{cores["amarelo"]}EMPATE{cores["limpa"]}')
    elif jogador == 2:
        print(f'VOCÊ {cores["verde"]}VENCEU{cores["limpa"]}')
elif cpu == 2:
    if jogador == 0:
        print(f'VOCÊ {cores["verde"]}VENCEU{cores["limpa"]}')
    elif jogador == 1:
        print(f'VOCÊ {cores["vermelho"]}PERDEU{cores["limpa"]}')
    elif jogador == 2:
        print(f'{cores["amarelo"]}EMPATE{cores["limpa"]}')
