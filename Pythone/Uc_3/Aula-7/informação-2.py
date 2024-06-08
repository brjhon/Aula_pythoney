#Faça um sistema que peça as informaçoes do curriculo de uma pessoa e imprima em um arquivo txt.

nome_arquivo = 'curriculo.txt'
conteudo ='Curriculo Online'
nome = input("Digite o seu Nome e Sobrenome : ")
idade = int (input("Digite a sua idade : "))
endereco = input("Digite o seu endereco : ")
objetivo = input("Digite o cargo/objetivo almejado : ")
skills = input("Digite as suas habilidades : ")
experiencia = ("Faça um breve resumo de suas experiencias anteriores : ")

def todo():
    return f"\n nome : {nome} \n idade : {idade} \n endereco: {endereco} \n objetivo : {objetivo} \n Habilidades: {skills} \n experiencia : {experiencia} "

# Abrir o arquivo no modo de escrita e escrever o conteudo
with open(nome_arquivo, 'w') as arquivo: #W = Write - ESCREVER
    arquivo.write(todo())
    
print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
print("Monte seu curriculo Online")

# Especificar o nome do arquivo a ser lido
nome_arquivo = 'curriculo.txt'

# Tentar abrir o arquivo no modo de leitura e ler o conteúdo
try:
    with open(nome_arquivo, 'r') as arquivo: # R = Read - LER
        conteudo = arquivo.read()
        print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}")
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")