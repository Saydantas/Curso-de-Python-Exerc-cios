'''Faça um algorítimo que leia o preço de um produto e montre seu novo preço com 5% de desconto'''

n = float(input('Qual o preço do produto? '))
d = n * 0.05
print(f'Valor à vista com desconto de 5% fica {n - d}R$')
