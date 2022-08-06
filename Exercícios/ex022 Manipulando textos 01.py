'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo sem considerar espaços.
- Quantas letras tem o primeiro nome.'''

n = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome completo em letras maiúsculas é {n.upper()}')
print(f'Seu nome complete em letras minúsculas ´é {n.lower()}')
print('Seu nome completo tem {} letras'.format(len(n) - n.count(' ')))
lista = n.split()
print(f'Seu primeiro nome é {lista[0]} e ele tem {len(lista[0])} letras')
