inventario = {"maçãs": 30, "bananas": 45, "laranjas": 25}

while True:
    acao = input("Digite 'adicionar' para acrescentar o estoque, 'mostrar' para ver o inventário, 'remover' para remover um produto ou 'sair' para sair: ")
    
    if acao == 'sair':
        break
    elif acao == 'adicionar':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))

        if produto in inventario:
            inventario[produto] += quantidade
            print(f"{quantidade} unidades de {produto} foram adicionadas ao inventário.")

        else:
            print("produto não encontrado no inventário")        


    elif acao == 'remover':
        produto = input("Digite o nome do produto que deseja remover completamente do inventário: ")
        if produto in inventario:
            del inventario[produto]
            print(f"{produto} foi removido do inventário.")
        else:
            print("Produto não encontrado no inventário.")

    elif acao == 'adição':
        produto = input("Digite o nome do produto que deseja adcionar ao inventário: ")
        inventario[produto] = dict()

    elif acao == 'mostrar':
        print("Inventário Atualizado:")
        for produto, estoque in inventario.items():
            print(f"{produto}: {estoque} unidades")

# Exibindo o inventário final
print("Inventário Final:")
for produto, estoque in inventario.items():
    print(f"{produto}: {estoque} unidades")