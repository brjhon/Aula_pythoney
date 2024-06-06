#Faza um programa que receba uma paralavra, se for "ping", retorne "pong" se for "time", retorne "Botafogo", se for "Vivo", retorna "morto'.


print("Seja bem vindo ao programa!")

Nome = input("Digite uma das paralavras (ping/time/vivo): ").lower()
def Cheke(a):

    if a == "ping":
        return "Pong" 
    
    elif a == "time":
        return "Botafogo"

    elif a == "vivo":
        return "Morto"

    else:
        return "Opção invalida"
    
print(Cheke(Nome))
