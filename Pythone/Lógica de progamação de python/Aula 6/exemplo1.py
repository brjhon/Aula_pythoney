cheklop  = int(input("Digite sua idade: ")) 
teck= input("Você é assinante do pass? (Sim/Não): ").lower()#O comando "lower" serve para modificar o texto

if cheklop >= 18 and teck == "sim": 
    #O comando funcional "and" como uma simplificação da  junção das variaveis
    print("Você Tem Acesso ao Game Pass!")

else:
    print("Você Não Tem Acesso ao Game Pass.")
