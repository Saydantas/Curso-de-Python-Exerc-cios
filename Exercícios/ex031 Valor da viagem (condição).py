'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

km = int(input('Digite a distância da sua viagem em Km: '))
if km <= 200:
    print(f'Sua viagem vai custar R${km * 0.50:.2f}')
else:
    print(f'Sua viagem vai custar R${km * 0.45:.2f}')
