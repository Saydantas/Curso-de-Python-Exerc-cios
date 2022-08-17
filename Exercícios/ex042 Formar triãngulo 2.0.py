'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os segmento acima PODEM FORMAR um triangulo', end=' ')  # end='' junta esse print com um dos de baixo
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:  #  eu sei que poderia ser só 'else'
        print('ISÓSCELES')
elif r1 + r2 < r3 or r2 + r3 < r1 or r3 + r1 < r2:
    print('Com essas medias NÃO PODEM FORMAR um triangulo ')
