'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

cidade = str(input('Digito o nome de uma cidade: ')).upper().strip()  # Coloca em maiúscula, e elimina os espaços
lista = cidade.split()  # coloca em uma lista
print('SANTO' in lista[0])  # analisa se o ‘item’ 0 da lista é igual a 'SANTO'
