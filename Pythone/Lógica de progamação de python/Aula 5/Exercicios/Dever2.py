Conometro = float(input("Quantos KM Irá percorrer?: "))
categoria = input("Qual a categoria?: ")


if categoria == "black":
   resultado = Conometro * 2
   print(f"O valor da corrida ficou: {resultado}") 

elif categoria == "confort":
   resultado = Conometro * 1.5
   print(f"O valor da corrida ficou: {resultado}") 

elif categoria == "convencional":
   resultado = Conometro * 1
   print(f"O valor da corrida ficou: {resultado}") 

elif categoria == "taxi":
   resultado = Conometro * 3
   print(f"O valor da corrida ficou: {resultado}") 

else:
   resultado = ("Você Escolheu a opção invalida")