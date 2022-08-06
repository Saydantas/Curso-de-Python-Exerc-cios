'''fatiamento'''
frase = 'Curso em Vídeo Python'
print(frase)  # aparece toda a frase
print(frase[9])  # aparece somente o caractere 9
print(frase[9:13])  # aparece do caractere 9 ao 12
print(frase[9:21])  # aparece até o fim da frase
print(frase[9:21:2])  # mostra do 9 ao 20, 1 letra sim e outra não
print(frase[:5])  # mostra do 0 ao 5
print(frase[15:])  # mostra do 15 até o fim
print(frase[9::3])  # mostra do 9 ao 20, 1 letra sim e 2 não
'''Análise'''
print(len(frase))  # exibe a quantidade de caracteres
print(frase.count('o'))  # exibe a quantidade de letras 'o' na frase
print(frase.count('o', 0, 13))  # exibe a quantidade de letas 'o' na frase, começando do 0 até o 12
print(frase.rfind('o'))  # exibe onde é encontrada a última letra 'o' (procura da direita para esquerda)
print(frase.find('deo'))  # exibe onde é encontrado na frase a palavra 'deo', onde ela se inicia
print(frase.find('Android'))  # exibe -1, pois a palavra não se encontra na frase
print('Curso' in frase)  # exibe se a palavra existe na frase
'''Transformação'''
print(frase.replace('Python', 'Android'))  # substitui a palavra 'Python' por 'Android
print(frase.upper())  # transforma todas as letras em maiúsculas
print(frase.lower())  # transforma todas as letras em minúsculas
print(frase.capitalize())  # transforma todas as letras em minúsculas, menos a primeira letra
print(frase.title())  # transforma a primeira letra de cada palavra em maiúsculas
frase2 = '   Aprenda Python  '
print(frase2)
print(frase2.strip())  # remove espaços inúteis
print(frase2.rstrip())  # remove espaços inúteis da direita
print(frase2.lstrip())  # remove espaços inúteis da esquerda
'''Divisão'''
print(frase.split())  # divide todas as palavras da frase e add em uma lista
'''junção'''
print(frase.split('-'.join(frase)))  # junta todas as palavras de uma lista
