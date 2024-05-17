list = []
numeroAtlet = 1

print("Por favor, insira a distancia dos lançamentos: ")
for i in range(10):
    #luping infinito de colocagem de atletas na lista um atleta, sengundo atleta, e assim por diante
    distancia = float(input(f"O atleta {i + 1} fez o lamçamento a qual distancia?: "))
    list.append(distancia)

for i in range(3):
    for distanciatlet in list:
        print(f"O Atleta {numeroAtlet + 1} lançou a distancia de {distanciatlet} metros")
        numeroAtlet += 1 #continua soma dos jogadores colocados 

    list.sort()
    list.reverse()
    print("Lançamento ordenados:", list)