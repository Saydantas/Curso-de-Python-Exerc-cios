'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, conforme a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL.')
elif imc <= 25:
    print('Parabéns! Você está no PESO IDEAL.')
elif imc <= 30:
    print('ALERTA! Você está com SOBREPESO.')
elif imc <= 40:
    print('CUIDADO! Você está em OBESIDADE.')
else:
    print('PERIGO! você está em OBESIDADE MÓRBIDA.')
