'''Crie um programa que mostre na tela todos os números pares no intervalo entre 1 e 50.'''

#  for c in range(1, 51):      # Conta do 1 ao 50
#      if c % 2 ==0:           # Se resto da divisão de 'c' por 2 for igual a zero
#          print(c, end=' ')   # Escreva 'c' na mesma linha
#  print('Acabou')

for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabou!')
