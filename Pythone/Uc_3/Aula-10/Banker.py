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

    def read_table_fields(table_name, fields):
        try:
            # Transforma a lista de campos em uma string separada por vírgula
            fields_str = ', '.join(fields)
            cursor.execute(f"SELECT {fields_str} FROM {table_name}")
            rows = cursor.fetchall()
            print(f"Dados de '{table_name}':")
            for row in rows:
                print(f"Preço: {row[0]}, Quilometragem: {row[1]}")
        except Error as e:
            print(f"Erro ao ler a tabela {table_name}: {e}")

    print("\nLeitura de 'nome' e 'Preço' e 'Quilometragem' das tabelas:")
    read_table_fields('caminhoes', ['nome','Preço', 'Quilometragem']),
    read_table_fields('carro', ['nome','Preço', 'Quilometragem']),
    read_table_fields('motos', ['nome','Preço', 'Quilometragem'])

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL encerrada")
