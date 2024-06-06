
# Tentar abrir o arquivo no modo de leitura e ler o conteúdo
nome = 'livro.txt'
Livronew = input("/n Deseja adcionarlivro? (sim/não): ").lower()

# Abrir o arquivo no modo de escrita e escrever o conteúdo
with open(nome, 'r') as arquivo:
    while Livronew != "não":
        titulo = input("Digite o titulo de um livro: ")
        autor = input("Digite o autor de um livro: ")
        print(f"Conteúdo do arquivo '{titulo}':\n{autor}")
        Livronew = input("/n Deseja adcionarlivro? (sim/não): ").lower()
        
    print(f"Conteúdo do arquivo '{nome}':\n{conteudo}")
    
