import random

print("Selecione o nível de dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")
level = int(input("Nível: "))
print()
print("Escolha o Inimigo")
print("1 - Aditron")
print("2 - Subtraira")
print("3 - Multiplac")
print("4 - Fraçãozor")
print("5 - Percentrox")
print("6 - Algebrion")
inimigo = int(input("Quem você deseja enfrentar agora? "))
print()
q = int(input('Quantas questões você quer responder? '))
print()
cont = 0
min_num = 0
max_num = 0
resp = 0
user_resp = 0
nun1 = 0
nun2 = 0

if level == 1:
    min_num = 1
    max_num = 25
elif level == 2:
    min_num = 1
    max_num = 50
elif level == 3:
    min_num = 1
    max_num = 100
else:
    print("Opção inválida")

if inimigo == 1:
    for i in range(1, q + 1):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        resp = num1 + num2

        print(f"Questão {i}: Qual é o resultado de {num1} + {num2}?")
        user_resp = int(input("Resposta: "))

        if user_resp == resp:
            print("Correto!")
            cont = cont + 1
        else:
            print(f"Incorreto. O resultado correto é {resp}.")
        print()

elif inimigo == 2:
    for i in range(1, q + 1):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        resp = num1 - num2

        print(f"Questão {i}: Qual é o resultado de {num1} - {num2}?")
        user_resp = int(input("Resposta: "))

        if user_resp == resp:
            print("Correto!")
            cont = cont + 1
        else:
            print(f"Incorreto. O resultado correto é {resp}.")
        print()

elif inimigo == 3:
    for i in range(1, q + 1):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        resp = num1 * num2

        print(f"Questão {i}: Qual é o resultado de {num1} * {num2}?")
        user_resp = int(input("Resposta: "))

        if user_resp == resp:
            print("Correto!")
            cont = cont + 1
        else:
            print(f"Incorreto. O resultado correto é {resp}.")
        print()

elif inimigo == 4:
    for i in range(1, q + 1):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        resp = Fraction = num1 / num2

        print(f"Questão {i}: Qual é o resultado de {num1} / {num2}?")
        user_resp = float(input("Resposta: "))

        if user_resp == resp:
            print("Correto!")
            cont = cont + 1
        else:
            print(f"Incorreto. O resultado correto é {resp}")
        print()

elif inimigo == 5:
    for i in range(1, q + 1):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        resp = num2 * num1 / 100

        print(f"Questão {i}: Qual é o resultado de {num1} % de {num2}?")
        user_resp = float(input("Resposta: "))

        if user_resp == resp:
            print("Correto!")
            cont = cont + 1
        else:
            print(f"Incorreto. O resultado correto é {resp}.")
        print()

print(f"Você conseguiu acertar {cont} de {q}")
print("Fim do programa. Pressione qualquer tecla para sair.")
input()
