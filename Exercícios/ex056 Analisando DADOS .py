'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
tothomem = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if sexo == 'M':
        tothomem += 1
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
if tothomem != 0:
    print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho.capitalize()}')
else:
    pass
if totmulher20 == 0:
    print('Não existe mulheres nesse grupo.')
elif totmulher20 == 1:
    print('Só existe 1 mulher com menos de 20 anos.')
else:
    print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
