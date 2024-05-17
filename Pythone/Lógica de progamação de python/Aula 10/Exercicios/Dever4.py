lista_atl =[]
NAtleta = 1 
print ("Por favor insira a distancia dos lançamentos atleticos: ")

for i in range(10):
    distance = float(input("O atleta { i + 1} fez o lançamento a qual distãncia: "))
    lista_atl.append(distance)

for distancePorAtl in lista_atl:
    print(f"O atleta {NAtleta} lançou a uma distacia de {distancePorAtl} metros")
    NAtleta + = 1

lista_atl.sort()
lista_atl.reserve()
print ("Lançamento ordenados: ", lista_atl)

