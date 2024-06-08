nome_pessoa = input("Digite o nome da pessoa para criar o arquivo: ").strip().replace(" ", "_").lower()
diretorio = r"C:\Users\62129532024.1\Documents\GitHub\Aula_pythoney\Pythone\Uc_3\Aula-7"
nome_arquivo = f"{diretorio}\\{nome_pessoa}_curriculo.html"

# Dicionário com os campos do 
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