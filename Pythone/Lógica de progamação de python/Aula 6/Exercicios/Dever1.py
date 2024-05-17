cart = input("Você tem o cartão black de acesso? (Sim/Não) ")
Vip = input("Você tem o Ingresso vip de acesso ao lounge? (Sim/Não) ").lower()

if cart == "sim" or Vip == "sim":
    print("Você tem acesso a sala vip!")
else:
    print("Você não tem acesso a sala vip!")
