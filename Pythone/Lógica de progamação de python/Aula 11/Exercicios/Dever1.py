import random #Importa uma biblioteca, que é usada para gerar números aleatorios.

print("Seja bem vindo ao jogo caça tesouro!") #Imprimi uma mensagem.
print("Tente encontrar o tesouro. Você tem 3 tentativas.") #Imprime uma mensagem.
print("Escolha um número entre 1 e 9 para procurar o tesouro.") # Está instruindo o jogador a escolher um número entre 1 a 9.

resultado = int(input("em qual casa está o tesouro")) #A variavel "resultado" guadara o resltado digitado pelo usúario.
tentaivas = 0 #Esta variavel será usada para contar o número de tentativas feitas pelo jogador.
randomn = random.randint(1,9) #Gera um número aleatorio entre 1 e 9. 

while resultado != randomn: #Este é um loop while que continua enquanto o número digitado.
    if tentaivas < 2: #É um condicional dentro do loop while que verifica se o número de tentativas é menor que 2
        print("Você Errou!")
        resultado = int(input("Em qual casa está o tesouso? "))
        tentaivas += 1

    else:
        print(f"Você expirou suas tentativas! estava no {aleatório}")
        break

if resultado == randomn:
    print("Você acertou!")