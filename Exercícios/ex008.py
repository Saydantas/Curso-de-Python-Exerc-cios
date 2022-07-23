'''Escreva um programa e o exiba convertido em Quilômetro, Hectômetro, decâmetro, Decímetro, Centímetro e Milímetros'''

n = float(input('Digite um valor em metros: '))
print(f'{n}m equivale a \n{n / 1000} km \n{n / 100} hm \n{n / 10} dam')
print(f'{n * 10} dm \n{n * 100} cm \n{n * 1000} mm')
