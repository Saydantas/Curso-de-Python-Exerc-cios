'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('Quantos Km você percorreu com o carro? '))
dia = float(input('Quantos dias passou com o carro? '))
print(f'O total a ser pago é R${(km * 0.15) + (dia * 60):.2f}')
