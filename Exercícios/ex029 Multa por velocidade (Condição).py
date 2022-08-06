'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = int(input('Digite a velocidade do seu carro: '))
if vel <= 80:
    print(f'Sua velocidade foi {vel}, para sua segurança não passe de 80km.')
else:
    print(f'Sua velocidade foi {vel}, você ultrapassou a velocidade limite, MULTADO!')
    print(f'Valor da Multa R${(vel - 80) * 7}')
