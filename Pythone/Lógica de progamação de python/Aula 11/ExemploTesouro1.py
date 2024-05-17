lista_tesouro = [1,2,3,4,5,6,7,8,9,10]
#indices = 0 a 9

Tesouro = 5
tentativas = 3

for contagem in lista_tesouro:
    escolher = int(input("Informe a posição que deseja tentar: "))
    tentativas -= 1
    if escolher == Tesouro:
        print("Parabéns, você achou o tesouro!")
        exit()

    else:
        print(f"Você errou. {tentaivas} chacer sobrando!")

    if tentaivas == 0:
        print("Você esgotou suas chaces. Programa encerrando...")
        quit()