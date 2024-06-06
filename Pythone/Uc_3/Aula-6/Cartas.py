#Faça um programa que lhe forneça 3 cartas de baralho e os ordene, onde A:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,J:9,Q:10,K:1
# Definição da função para ordenar as cartas
def ordenar_cartas(cartas):
    valores = {'A': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 11, 'K': 12}
    cartas_ordenadas = sorted(cartas, key=lambda carta: valores[carta[1]])
    return cartas_ordenadas

def main():
    cartas = []

    for i in range(3):
        carta = input(f"Digite a {i + 1}ª carta: ").upper()
        cartas.append(carta)

    cartas_ordenadas = ordenar_cartas(cartas)

    print("Cartas ordenadas:", cartas_ordenadas)

if __name__ == "__main__":
    main()
