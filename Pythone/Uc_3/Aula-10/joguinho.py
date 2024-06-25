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


import mysql.connector
from mysql.connector import Error

# Configuração da conexão
config = {
    'user': 'root',
    'password': '',  # Substitua pelo seu password
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

try:
    # Conectando ao servidor MySQL
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print("Conectado ao servidor MySQL")

    cursor = conn.cursor()

    # Listar todos os bancos de dados
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print("Databases available:")
    for db in databases:
        print(db[0])

    # Selecione o banco de dados correto
    database_name = 'auto'

    if (database_name,) in databases:
        conn.database = database_name
        print(f"Usando o banco de dados '{database_name}'")
    else:
        print(f"Database '{database_name}' não encontrado. Por favor, verifique o nome do banco de dados.")
        cursor.close()
        conn.close()
        exit()

    # Função para ler dados específicos de uma tabela
    def read_table_fields(table_name, fields):
        try:
            # Transforma a lista de campos em uma string separada por vírgula
            fields_str = ', '.join(fields)
            cursor.execute(f"SELECT {fields_str} FROM {table_name}")
            rows = cursor.fetchall()
            print(f"Dados da tabela '{table_name}':")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Erro ao ler a tabela {table_name}: {e}")

    # Lendo dados específicos das tabelas
    print("\nLeitura de dados específicos:")
    read_table_fields('caminhoes', ['Preço', 'Quilometragem'])
    read_table_fields('carro', ['Preço', 'Quilometragem'])
    read_table_fields('motos', ['Preço', 'Quilometragem'])

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL encerrada")
