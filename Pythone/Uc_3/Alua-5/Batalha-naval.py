# Criar uma jogo "Batalha naval"
#Deverá ser possível colocar submarinos, que são barcos que ocupam 1 de espaço na matriz inicialmente 
#serão colocados de maneira aleatória e o usuário não saberá onde ficarão posicionados.

import random
def verificar_tesouro(indici, locais):
    if locais[indici] == 1:
        return(True)
    
    else:
        return (False)
    


def main():
    print("Bem vindo ao jogo de batalha naval!")
    print("Escolha um número entre 1 e 10 para procurar o tesouro.")

    # Define o número de tentativas 
    tentativas = 3
    print("Tente encontrar o tesouro. Voce tem 3 tentativas. ")
    print("Escolha um número entre 0 e 9 para procurar o tesouro. ")
    #Inicializa o contador de tentativas 
    contador = 0

