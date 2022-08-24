'''Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep
print('Vamos começar a contagem? ')
n = str(input('Digite S ou N: ')).upper()
if n == 'S':
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('BUM! BUM! POOOW!')
elif n == 'N':
    print('Assim que estiver proto inicie o programa!')
else:
    print('OPÇÃO INVÁLIDA!')
