'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        cont = cont + 1
        s = s + num
print(f'Você informou {cont} Números pares e a soma deles é {s}')
