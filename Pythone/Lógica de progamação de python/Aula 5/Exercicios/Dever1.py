# Um programa que funciona para escolher a categoria de algo, nesse caso, categorias de carro
Car = int(input("Qual o numero da categoria do Carro?"))

if Car == 1:
    resultado = ("Você acabou de pedir um Carro BLACK")

elif Car == 2:
    resultado = ("Você acabou de pedir um Carro CONFORT")

elif Car == 3:
     resultado = ("Você acabou de pedir um Carro CONVENCIONAL")

elif Car == 4:
    resultado = ("Você acabou de pedir um Carro TAXI")

else:
    resultado = ("Você selecionou a opção errada")

print(resultado)
