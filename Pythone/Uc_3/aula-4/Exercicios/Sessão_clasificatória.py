#Faça um programa que simule uma sessão classificatória de Formula 1. 
#Onde recebera o nome e o melhor tempo de um piloto.
nome_6Q1, tempo_6Q1 = [], []
nome_6Q2, tempo_6Q2 = [], []
nome_6Q3, tempo_6Q3 = [], []


name = input("Digite 10 nomes dos pilotos e o melhor tempo percorrido de cada um, clasificação(nome:tempo):  ")

for i in range(5):
    entrada = input (f"piloto {i+1}: ")
    
    nome = entrada[0]
    tempo = float(entrada[1])
    
    nome_6Q1.append(name.split("nome")[i])
    tempo_6Q1.append(name.split("tempo")[i + 1])
    print(nome_6Q1 + tempo_6Q1)

