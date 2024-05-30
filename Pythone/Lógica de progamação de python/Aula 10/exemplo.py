#Definir uma lista com elementos repitidos.
lista = [1, 2, 2, 3, 4, 4, 5] # Cria para colocar em uma planilha.
elemento = 4 
#Escolha de uns dos números na planilha.

#Contar quantos vezes o elemento aparece.
quantidade = lista.count(elemento)
# Pegando a quantidade de números repetidos escolhidos.
print(f"O elemento {elemento} aparece {quantidade} vezes na lista que tem um total de {len(lista)} elemento.")
