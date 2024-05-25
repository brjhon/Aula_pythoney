Print("Programa de avaiação de Carro")

avaliação = int(input("Escolha qual e a Qualificação de seu carro, opções:/n 1: 0 a 50/n 2: 50 a 80/n 3: 80 a 100% /n escolha uma opão: "))
Carro = int(input("Qual e o carro: "))

if avaliação == 1:
    print(f"A avaliação de seu {Carro} de 0% para 50%")

elif avaliação == 2:
        print(f"A avaliação de seu {Carro} de 50% para 80%")

elif avaliação == 3:
        print(f"A avaliação de seu {Carro} de 80% para 100%")

elif avaliação == 4:
    break

else:
    print("Você escolheu uma opção invalida")
break