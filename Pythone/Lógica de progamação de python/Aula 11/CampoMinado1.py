
# lista com Dez espaços inicialmente vazios (representados por 0)
locais = [0,0,1,0,0,0,0,0,0,0]

#Define o número de Tentativas
Tentativas = 3 
print("Bem vindo ao jogo de caça ao tesouro!")
print("Tente encontrar o tesouro. Voc~e tem 3 tentativas. ")

#Inicializa o contador de tentativas 
contador = 0 

# Um Loop para as tentativas do Usuário ate ele der um valor desejado
while contador != Tentativas 
    contador += 1 
    palpite = int(input("Escolha um indice para procurar o tesouro: "))
    if 0 <= palpite <= 9:#Verificação se o palpite está dentro do intervalo
        if locais[palpite] == 1:
            print("Voce encontrou")
        else:
            print("Não é esse o local do tesouro. Tente novamente.")
        
    else:
        print("Por favor, insira um número entre 0 e 9.")

if(contador == Tentativas):
    print(f"Suas tentativas acabarma! O tesouro estava no índice. ")
