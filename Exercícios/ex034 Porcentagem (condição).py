'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

sal = float(input('Digite seu salário para calcular o aumento: '))
if sal <= 1250:
    print(f'Seu novo salário é R$ {(sal * 15 / 100) + sal:.2f}')
else:
    print(f'Seu novo salário é R$ {(sal * 10 / 100) + sal:.2f}')
