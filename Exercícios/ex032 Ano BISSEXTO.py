'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

from datetime import date
ano = int(input('Que ano você quer analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')
# legenda da fórmula: ano, resto da divisão por 4 tem que ser
# igual a 0, ano resto da divisão por 100 diferente de 0
# ou resto da divisão de ano por 400 igual a 0
