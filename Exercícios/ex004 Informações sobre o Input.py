"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis 
sobre ele."""

n = input('Digite Algo ')
print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É Alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em maiúsculo? {n.isupper()}')
print(f'Está em minúsculo? {n.islower()}')
print(f'Está capitalizada? {n.istitle()}')
