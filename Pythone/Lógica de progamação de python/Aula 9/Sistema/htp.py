from blibioteca import som #importação de uma blibioteca pronta em outro local
from blibioteca import dobro #importação de uma blibioteca pronta em outro local
from blibioteca import Div #importação de uma blibioteca pronta em outro local
from blibioteca import Sub #importação de uma blibioteca pronta em outro local

resultado = 0

while True:  
    
    Conometro = int(input("escolha um número entre [1, 2, 3, 4]:  ")) 
    #Escolha do usúario para ter algum resultado.

    if Conometro == 1:
        resultado = int(input("Digite algum número que deseja somar: "))
        media = som(resultado)
        print(f"O Resultado e: {media}") #aqui esta iniciando um comando para printar o calculo.


    elif Conometro == 2:
        resultado = int(input("Digite algum número que deseja somar: "))
        media = dobro(resultado) #A variavel "media" esta guardando o calculo que esta na importação.
        print(f"O Resultado e: {media}") 

    elif Conometro == 3:
        resultado = int(input("Digite algum número que deseja somar: ")) #Guardara dados que o usúario esta colocando.
        media = Div(resultado)
        print(f"O Resultado e: {media}") 

    elif Conometro == 4: #Esse comando resultara na escolha que o usúario decidir.
        resultado = int(input("Digite algum número que deseja somar: "))
        media = Sub(resultado)
        print(f"O Resultado e: {media}") 

    elif Conometro == 5:
        break #Utilizado para finalizar o programa caso o usúario escolha outra opção

    else:
        print(f"Você Escolheu a opção invalida")
    break # Serve para não ficar rodando infinitamente
        
   