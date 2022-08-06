'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = str(input('Digite seu nome completo: ')).upper().strip()
lista = nome.split()  # coloca as palavras em uma lista
print('SILVA' in lista)  # Verifica se existe a palavra SILVA na lista.
