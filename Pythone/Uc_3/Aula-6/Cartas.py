#Faça um programa que lhe forneça 3 cartas de baralho e os ordene, onde A:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,J:9,Q:10,K:1
import random  # Importa o módulo random para gerar números aleatórios

# Função para gerar três números aleatórios
def gerar_numeros():
    return [random.randint(0, 12) for i in range(3)]

# Função para ordenar os números usando um método simples de ordenação
def ordenar_numeros(lista_numeros):
    for i in range(len(lista_numeros)):
        for j in range(i + 1, len(lista_numeros)):
            if lista_numeros[i] > lista_numeros[j]: 
                lista_numeros[i], lista_numeros[j] = lista_numeros[j], lista_numeros[i]
    return lista_numeros

# Função para converter números manualmente
def converter_numeros(lista_numeros):
    # Dicionário de conversão de números para caracteres
    mapeamento = {0: 'A', 10: 'J', 11: 'Q', 12: 'K'}
    numeros_convertidos = []
    for numero in lista_numeros:
        if numero in mapeamento:
            numeros_convertidos.append(mapeamento[numero])
        else:
            numeros_convertidos.append(numero)
    return numeros_convertidos

# Gerar três números aleatórios
numeros_aleatorios = gerar_numeros()
print(f"Números gerados: {numeros_aleatorios}")

# Ordenar os números
numeros_ordenados = ordenar_numeros(numeros_aleatorios)

# Converter os números
numeros_convertidos = converter_numeros(numeros_ordenados)
print(f"Números ordenados e convertidos: {numeros_convertidos}")