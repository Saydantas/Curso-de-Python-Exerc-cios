'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e
que se encontram no intervalo de 1 até 500.'''
s = 0
cont = 0
for c in range(1, 501, 2):  # Conta de 1 até 500 pulando a cada 2
    if c % 3 == 0:          # Verifica se resto da divisão de 'c' por 3 é igual a 0
        cont = cont +1      # Conta quantas vezes foi repetido a estrutura
        s = s + c           # Soma todos os números verificados nas condições do 'if'
print(f'A soma de todos os números ímpares divisíveis por 3 entre 1 e 500 é {s}\n'
      f'E existem {cont} números nessas condições.')
