'''Escreva um programa que leia dois números inteiros e compare-os. Mostrando uma mensagem na tela:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print(f'O PRIMEIRO número é maior.')
elif n2 > n1:
    print(f'O SEGUNDO número é maior.')
else:
    print('Os valores são iguais.')
