#pedidos ao usúario para inserir três valores
entrada = input("Digite três separadas por vírgulas: ")
valores = entrada.split(",")    #Isso cria uma lista dos valores
minha_tupla = tuple(valores)    #Convertendo a lista em uma tupla

#Mostrando cada elemento da tupla
print("Os valores inseridor foram: ")
for elemento in minha_tupla: 
    print(elemento)

