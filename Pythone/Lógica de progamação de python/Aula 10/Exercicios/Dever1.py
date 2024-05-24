#Faça um programa para uma cafeteria automatizada. 
# Onde tem 5 tipos de café. Cada cadé demora um tempo específico para der jeito.
# Deverá mostrar a contagem regressiva de tempo para ele ser feito e depois mostrar
#uma mensagem de Sucesso.

#Cafés:
#Expresso - 10R$
#Tradicional - 15R$
#CApuccino - 22R$
#Latter - 18R$
#Descapuccino - 20R$

Expresso = int(10)
Tradicional = int(15)
Capuccino = int(22)
Latter = int(18)
Descapuccino = int(20)

#parte do pagamento do café
senha = int(input("Digite a senha do seu cartão de Debito: "))
senha1 = int(input("Digite a senha do seu cartão de Credito: "))

cafeteria = int(input(f"Digite 1 para 'Expresso',\n digite 2 para 'Tradicional',\n digite 3 para 'Capuccino',\n digite 4 para 'Latter',\n digite 5 para 'Descapuccino': "))

if cafeteria == 1:
    for Expresso in range(10,0,-1):
        print(f"O Café: {Expresso}")
    print(f"Café pronto ele custou 10R$ ")

    cart = input(f"Escolha uma aforma de pagamento: \ncredito ou debito: ")
    if cart == 'debito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha
        print("Pagamento concluido")

    elif cart == 'credito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha1
        print("Pagamento concluido")

    else:
        print("Senha invalida")

elif cafeteria == 2:
    for Tradicional in range(10,0,-1):
        print(f"O Café: {Tradicional}")
    print(f"Café pronto ele custou 15R$")

    cart = input(f"Escolha uma aforma de pagamento: \ncredito ou debito: ")
    if cart == 'debito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha
        print("Pagamento concluido")

    elif cart == 'credito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha1
        print("Pagamento concluido")

    else:
        print("Senha invalida")

elif cafeteria == 3:
    for Capuccino in range(10,0,-1):
        print(f"O Café: {Capuccino}")
    print(f"Café pronto ele custou 22R$")

    cart = input(f"Escolha uma aforma de pagamento: \ncredito ou debito: ")
    if cart == 'debito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha
        print("Pagamento concluido")

    elif cart == 'credito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha1
        print("Pagamento concluido")

    else:
        print("Senha invalida")

elif cafeteria == 4:
    for Latter in range(10,0,-1):
        print(f"O Café: {Latter}")
    print(f"Café pronto ele custou 18R$")

    cart = input(f"Escolha uma aforma de pagamento: \ncredito ou debito: ")
    if cart == 'debito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha
        print("Pagamento concluido")

    elif cart == 'credito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha1
        print("Pagamento concluido")

    else:
        print("Senha invalida")

elif cafeteria == 5:
    for Descapuccino in range(10,0,-1):
        print(f"O Café: {Descapuccino}")
    print(f"Café pronto ele custou 20R$")

    cart = input(f"Escolha uma aforma de pagamento: \ncredito ou debito: ")
    if cart == 'debito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha
        print("Pagamento concluido")

    elif cart == 'credito':
        num = int(input(f"Digite a senha do seu cartão de debito: "))
        num == senha1
        print("Pagamento concluido")

    else:
        print("Senha invalida")
    
else:
    print("Erro")

