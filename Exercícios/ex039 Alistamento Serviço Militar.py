'''Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo.'''

#  from datetime import date
#  ano = int(input('Digite seu ano de nascimento: '))
#  n = date.today().year - ano
#  if n < 18:
#      print(f'Você completa {n} anos em {date.today().year}, ainda não pode se alistar.')
#  elif n == 18:
#      print(f'Você completa {n} anos em {date.today().year}, compareça a junta de serviço militar.')
#  else:
#      print(f'Você completa {n} anos em {date.today().year}, está atrasado para o alistamento militar.')

from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} completa {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o seu alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria te se alistado há {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
