tempo = int(input('qual o ano do seu carro? '))  # grava um número inteiro
# print('carro novo' if tempo <= 3 else 'carro velho')
if tempo <= 3:  # se tempo for menor ou igual a 3
    print('Seu carro é novo.')  # escreva: Seu carro é novo
else:  # se não
    print('Seu carro é velho')  # escreva: Seu carro é velho
print('--FIM--')  # escreva --FIM--

nome = str(input('Qual é o seu nome? ')).upper()  # grava o nome do usuário e coloca tudo em maiúsculo
if nome == 'THIAGO':  # Se nome for igual a 'THIAGO'
    print('Que nome lindo você tem!')  # Escreve
else:  # Se não
    print('Seu nome é tão comum!')  # Escreve
print(f'Bom dia, {nome.capitalize()}!')  # Escreve o nome com a primeira letra maiúscula

n1 = float(input('Digite a primeira nota: '))  # Grava a primeira nota
n2 = float(input('Digite a segunda nota: '))  # Grava a segunda nota
m = (n1 + n2) / 2  # média igual à soma das notas divido por 2
print(f'A sua média foi {m}')  # escreve a média
# print('Parabéns!' if m >= 6 else 'Estude mais!')
if m >= 6:  # Se m for maior ou igual a 6
    print('Parabéns')  # Escreva
else:  # se não
    print('Estude mais')  # Escreva
