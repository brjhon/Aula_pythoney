#Faça m programa que  me permita somar N números que o usúario queria da sequencia de fibonacci.
#Retorne quantos números primos tem nessa sequência de N números e quais são eles

""" x = int(input("Digite algum número que deseja ser somado: "))
lista = []
for bla in range(0,x):
 y = x + 1
 n = x + y
 lista.append()

print(f"Os números que foram somados são esses: {n}") """

# Use esse 
numero = int(input("Até quantos números deseja que var?: "))

if Num <= 1: 
    print(f"{Num} é primo")

elif numero % 2 == 0 or numero % 3 == 0:
    print(f"{numero} não é primo")

elif numero <= 3:
    priint  (f"{numero} é primo")

else:
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            print(f"{numero} não é primo")
            break   
        i +=6    
    else:
        print(f"{numero} é primo")