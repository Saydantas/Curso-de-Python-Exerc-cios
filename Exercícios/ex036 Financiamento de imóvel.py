''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.'''

val = float(input('Qual o valor da casa que deseja comprar? '))
sal = float(input('Qual valor do salário que você recebe? '))
ano = int(input('Em quantos anos pretende pagar? '))
mes = ano * 12
parc = val / mes
if parc >= sal - (sal * 70 / 100):
    print(f'Para pagar uma casa de {val:.2f} em {ano} anos a prestação será de {parc:.2f} \nEmpréstimo NEGADO!')
else:
    print(f'Para pagar uma casa de {val:.2f} em {ano} anos a prestação será de {parc:.2f} \nEmpréstimo APROVADO!')
