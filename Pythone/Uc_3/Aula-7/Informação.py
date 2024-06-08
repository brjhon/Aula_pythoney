#Faça um programa que peça as imformações do corriculo de uma pessoa e imprema em uma arquivo.txt 

nome_arquivo = input("Escolha nome para o arquivo.txt: ")

# Abrir o arquivo no modo de escrita
with open(nome_arquivo, 'w') as arquivo:
    Livronew = 'sim'

    while Livronew == "sim":
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        sexo = input("Digite seu sexo: ")
        profissao = input("Digite sua profissão: ")
        
        conteudo = f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}\nProfissão: {profissao}\n"
        arquivo.write(conteudo)
        Livronew = input("Deseja corrigir algo? (sim/não): ").lower()
        break
        
    print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}")

