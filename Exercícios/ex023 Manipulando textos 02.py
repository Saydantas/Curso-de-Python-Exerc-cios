'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10  # faz a divisão inteira  por 1 e mostra o resto da divisão
d = num // 10 % 10  # faz a divisão inteira por 10 e mostra o resto da divisão
c = num // 100 % 10  # faz a divisão inteira por 100 e mostra o resto da divisão
m = num // 1000 % 10  # faz a divisão inteira por 1000 e mostra o resto da divisão
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
