'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print(f'Nessa frase a letra "A" aparece {frase.count("A")}x')  # Mostra quantas letras A aparecem
print(f'A primeira vez que a letra "A" aparece e na posição {frase.find("A") + 1}')  # Mostra a pos da primeira letra A
print(f'A ultima vez que a letra "A" aparece e na posição {frase.rfind("A") + 1}')  # Mostra a posição da última letra A
