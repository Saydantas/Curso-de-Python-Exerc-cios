'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
cont = 0
ano = date.today().year
for c in range(1, 8):
    n = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if ano - n >= 18:
        cont = cont + 1
if cont == 1:
    print('Só existe 1 pessoa maior de idade.')
else:
    print(f'Entre os anos informados existem {cont} pessoas maiores de idade.')
    print(f'E as outras {7 - cont} pessoas não são maiores de idade')
