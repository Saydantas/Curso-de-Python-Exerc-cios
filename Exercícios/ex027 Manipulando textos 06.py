'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.'''

nome = str(input('Digite o nome completo: ')).strip()
lista = nome.split()  # Coloca o nome em uma lista
print(f'Seu primeiro nome é {lista[0].capitalize()}')  # Exibe o primeiro nome da lista
print(f'Seu último nome é {lista[len(lista)-1].capitalize()}')  # Exibe o último nome da lista
