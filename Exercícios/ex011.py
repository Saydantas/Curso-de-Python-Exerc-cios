'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m² '''

al = float(input('Digite a altura: '))
lar = float(input('Digite a largura: '))
m = al * lar
print(f'Sua parede tem {m}m² você vai precisar de {m / 2} litros de tinta para pintá-la')
