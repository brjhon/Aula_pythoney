lista = input("Digite 5 nomes desconhecidos, separando eles com virgulas: ")
Valor = lista.split(",") #Tranformando uma list em uma tupla
my_tupla = tuple(Valor)

if len(lista) != 5:
    print("Voce não inseriu 5 nomes")

else:
    nome_inserido = input("Digite um nome para verificação na lista: ")

    if nome_inserido in my_tupla:
        print(f"O nome {nome_inserido} está na lista")
    else:
        print(f"O nome {nome_inserido} não está na lista")
        
    print("Voce escolheu um nome que não está na lista")
