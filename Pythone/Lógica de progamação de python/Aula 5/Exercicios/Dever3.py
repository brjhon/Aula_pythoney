nome = input("Qual o nome do clinte?: ")
Trem = int(input("Quantos metros de tapete?: "))
tapete = input("Qual a qualidade do tapete")

if tapete == "convencional":
   Medida = Trem * 10
   print(f"Olá {nome} o valor do seu orçamento ficou {Medida}")

elif tapete == "premium":
   Medida = Trem * 20
   print(f"Olá {nome} o valor do seu orçamento ficou {Medida}")

elif tapete == "maxpremium":
   Medida = Trem * 30
   print(f"Olá {nome} o valor do seu orçamento ficou {Medida}")
   
else: print("ORÇAMENTO INCORRETO")





















