#import numpy as np

#def jogo_batalha_naval(tamanho_tabuleiro=5):
    # Criando o tabuleiro com zeros
 #   tabuleiro = np.zeros((tamanho_tabuleiro, tamanho_tabuleiro), dtype=int)
    
    # Posicionando o navio de forma aleatória
#    posicao_navio = (np.random.randint(0, tamanho_tabuleiro), np.random.randint(0, tamanho_tabuleiro))
    
    # Variáveis adicionais
#    tentativas = 0
#    acertou = False
    
#    print("\nBem-vindo ao Jogo de Batalha Naval!")
#    print(f"Um navio está escondido em um tabuleiro {tamanho_tabuleiro}x{tamanho_tabuleiro}. Boa sorte!\n")
    
#    while not acertou:
#        print("Tabuleiro:")
#        print(tabuleiro)
        
        # Recebendo palpite do usuário
#        try:
#            linha = int(input(f"Adivinhe a linha (0-{tamanho_tabuleiro-1}): "))
#            coluna = int(input(f"Adivinhe a coluna (0-{tamanho_tabuleiro-1}): "))
            
            # Verificando se o palpite está dentro dos limites do tabuleiro
#            if linha < 0 or linha >= tamanho_tabuleiro or coluna < 0 or coluna >= tamanho_tabuleiro:
#                print(f"Por favor, insira valores dentro do intervalo de 0 a {tamanho_tabuleiro-1}.")
#                continue
#        except ValueError:
#            print("Por favor, insira um número inteiro válido.")
#            continue
        
#        tentativas += 1
        
        # Verificando se o palpite acertou o navio
#        if (linha, coluna) == posicao_navio:
#            print(f"Parabéns! Você acertou o navio em {tentativas} tentativas!")
#            acertou = True
#        else:
#            if tabuleiro[linha, coluna] == -1:
#                print("Você já tentou essa posição. Tente novamente.")
#            else:
#                tabuleiro[linha, coluna] = -1
#                print("Errou! Tente novamente.\n")

# Exemplo de execução do jogo
#jogo_batalha_naval()


import numpy as np

def jogo_batalha_naval():
    tabuleiro = np.zeros((5, 5), dtype=int)
    posicao_navio = (np.random.randint(0, 5), np.random.randint(0, 5))
    tentativas = 3
    acertou = False
    
    while not acertou:
        print("\nTabuleiro:")
        print(tabuleiro)
        linha = int(input("Adivinhe a linha (0-4): "))
        coluna = int(input("Adivinhe a coluna (0-4): "))
        tentativas += 1
        if (linha, coluna) == posicao_navio:
            print(f"Você acertou o navio em {tentativas} tentativas!")
            acertou = True
        else:
            tabuleiro[linha, coluna] = - tentativas
            print("Errou! Tente novamente.")

jogo_batalha_naval()