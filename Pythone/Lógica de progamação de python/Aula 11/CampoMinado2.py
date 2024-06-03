import random

def verificar_tesouro(indici, locais):
    if locais[indici] == 1:
        return(True)
    
    else:
        return (False)


# Lista com Dez espaços inicialmente vazios (representados por 0)
locais = [0] * 10

# Coloca o tesouro (representa pelo número 1) em um índice aleatório
lugar_tesouro = random.randint(0,9)
locais [ lugar_tesouro]

# Define o número de tentativas 
tentativas = 3
print("Bem vindo ao jogo de caça ao tesouro!")
print("Tente encontrar o tesouro. Voce tem 3 tentativas. ")
print("Escolha um número entre 0 e 9 para procurar o tesouro. ")
#Inicializa o contador de tentativas 
contador = 0 

# Um Loop para as tentativas do Usuário ate ele der um valor desejado
while contador != tentativas:
    contador += 1 
    palpite = int(input("Escolha um indice para procurar o tesouro: "))
    if 0 <= palpite <= 9:#Verificação se o palpite está dentro do intervalo
        if verificar_tesouro(palpite, locais) == True:
            print("Parabés! Voce encontrou o tesouro!")
            break
        else:
            print("Não é esse o local do tesouro. Tente novamente.")
        
    else:
        print("Por favor, insira um número entre 0 e 9.")

if(contador == tentativas):
    print(f"Suas tentativas acabarma! O tesouro estava no índice {lugar_tesouro}. ")