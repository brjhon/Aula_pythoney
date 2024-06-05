# Criar uma jogo "Batalha naval"
#Deverá ser possível colocar submarinos, que são barcos que ocupam 1 de espaço na matriz inicialmente 
#serão colocados de maneira aleatória e o usuário não saberá onde ficarão posicionados.

#Inicio no codigo
from random import randint

# ---- Confuguração do tabuleiro ----

board_size = 5  # Tamanho do tabuleiro (5x5 neste exemplo)
board = [['O' for _ in range(board_size)] for _ in range(board_size)] # Nesta lina: E a criação do tabuleiro como uma matriz bidimensional usando listas de compreensão.
#Cada celula do tabuleiro e inicializada com '0', informando água.

def print_board(board):
    for row in board:
        print(' '.join(row))

print_board(board)
                                          # ---- PARTE LEGAL ----
# ---- Posicionamento dos Navios. ----
def place_ship(board):
    ship_row = randint(0, board_size - 1)#Gera aleatoriamente um número inteiro entre 0 e board_size - 1, que representa a linha onde o navio será posicionado.
    ship_col = randint(0, board_size - 1)
    board[ship_row][ship_col] = 'X' #Define a célula do tabuleiro na posição gerada aleatoriamente
                                    #como 'X'
    return ship_row, ship_col # Retorna as cordenadas (Linha/Coluna)

ship_row, ship_col = place_ship(board) #Posiciona o navio e obtem as coordenadas dele.
print_board(board)
#Imprime o tabuleiro atualizado.


# ---- Jogada do jogador. ----
def player_move(board):
    while True:
        try:
            row = int(input("Informe a linha (0-4): "))
            col = int(input("Informe a coluna (0-4): "))
            if 0 <= row < board_size and 0 <= col < board_size:
                return row, col
            else:
                print("Por favor, insira valores dentro do intervalo permitido.")
        except ValueError:
            print("Por favor, insira valores numéricos.")

player_row, player_col = player_move(board)

# ---- Verificação da Jogada ----
def check_move(board, row, col):
    if board[row][col] == 'X':
        print("Parabéns! Você acertou o navio!")
        board[row][col] = '!'
    else:
        print("Você errou. Tente novamente.")
        board[row][col] = '.'

check_move(board, player_row, player_col)
print_board(board)



