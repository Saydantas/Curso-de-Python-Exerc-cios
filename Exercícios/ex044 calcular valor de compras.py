'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

preço = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro/PIX\n'
      '[ 2 ] à vista no cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual sua opção? '))
if opção == 1:
    print(f'Suas compras no valor de {preço} à vista tem 10% de desconto e fica {preço - (preço * 10 / 100)}')
elif opção == 2:
    print(f'Suas compras no valor de {preço} à vista no cartão tem 5% de desconto e fica {preço - (preço * 5 / 100)}')
elif opção == 3:
    print(f'Suas compras no valor de {preço} ficam em 2x de {preço / 2}')
elif opção == 4:
    parcelas = int(input('Em quantas parcelas? '))
    valorp = preço + (preço * 20 / 100)
    print(f'Suas compras no valor de {preço} vai custar {valorp} em {parcelas}x de {valorp / parcelas}')
elif opção >= 5:
    print('OPÇÂO INVALIDA! tente novamente.')
