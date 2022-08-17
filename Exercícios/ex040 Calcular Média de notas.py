'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
conforme a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Sua média foi {m:.2f}, você ficou REPROVADO!')
elif 5 <= m < 7:
    print(f'Sua média foi {m:.2f}, Você ficou em RECUPERAÇÃO! ')
else:
    print(f'Sua média foi {m:.2f}, você está APROVADO!')
