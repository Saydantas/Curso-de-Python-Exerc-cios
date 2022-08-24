'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

'''frase = str(input('Digite uma frase: ')).strip().upper() # elimina os espaços e coloca tudo para maiusculo.
palavra = frase.split() # separa numa lista
junto = ''.join(palavra) # junta todas as palavras sem espaços
inverso = '' # inverso sem espaços
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')'''


frase = str(input('Digite uma frase: ')).strip().upper() # elimina os espaços e coloca tudo para maiusculo.
palavra = frase.split() # separa numa lista
junto = ''.join(palavra) # junta todas as palavras sem espaços
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
