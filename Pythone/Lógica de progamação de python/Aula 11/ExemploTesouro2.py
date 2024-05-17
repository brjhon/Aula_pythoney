tentaivas = 3
tesouro = 0
contador = 0

while contador < tentaivas:
    contador += 1
    tesouro = int(input("Informe a posição que deseja tentar: "))

    if tesouro == 3:
        print("Você achou! O tesouro estava na casa 3!")
        break

    print(f"Você errou. {tentaivas} chances sobrando!")

if tentaivas == 0:
    print("Você esgotou as tentativas. programa encerrando...")

