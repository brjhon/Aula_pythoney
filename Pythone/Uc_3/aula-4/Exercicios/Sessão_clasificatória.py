#Faça um programa que simule uma sessão classificatória de Formula 1. 
#Onde recebera o nome e o melhor tempo de um piloto.
""" clasificação1 = [], []
clasificação2= [], []
clasificação3 = [], []


name = input("Digite 10 nomes dos pilotos e o melhor tempo percorrido de cada um, clasificação(nome:tempo):  ")
#Max Verstappen Sergio Pérez Lewis Hamilton Fernando Alonso Carlos Sainz Jr Charles Leclerc Lando Norris 
for i in range(10):
    
    name = input(f"piloto {i+1}: ")
    tempo = input(f"tempo {i+1}: ")
    clasificação1.append(name)
    entrada = input (f"piloto {i+1}: ")
    print(nome_6Q1 + tempo_6Q1)
 """

# matrizes para armazenar os dados das classificatórias
classificatoria1= [], []
classificatoria2= [], []
classificatoria3 =[], []

# Coletando dados para a primeira classificatória com 7 pilotos
print("Digite o nome e o melhor tempo dos 7 pilotos da primeira classificatória (nome:tempo):")
for i in range(3):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]
    tempo = float(entrada[1])
    classificatoria1.append(nome,tempo)


# Coletando dados para a segunda classificatória com 5 pilotos
print("Digite o nome e o melhor tempo dos 5 pilotos da segunda classificatória (nome:tempo):")
for i in range(2):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]
    tempo = float(entrada[1])
    classificatoria2.append(nome,tempo)

# Coletando dados para a terceira classificatória com 3 pilotos
print("Digite o nome e o melhor tempo dos 3 pilotos da terceira classificatória (nome:tempo):")
for i in range(2):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]
    tempo = float(entrada[1])
    classificatoria3.append(nome,tempo)

# Imprimindo as matrizes das classificatórias
print("\nResultados da Primeira Classificatória:")
print("Pilotos: ")
for nome in classificatoria1:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in classificatoria1:
    print(f"{tempo:.2f} segundos", end=", ")

print("\n\nResultados da Segunda Classificatória:")
print("Pilotos: ")
for nome in classificatoria2:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in classificatoria2:
    print(f"{tempo:.2f} segundos", end=", ")

print("\n\nResultados da Terceira Classificatória:")
print("Pilotos: ")
for nome in classificatoria3:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in classificatoria3:
    print(f"{tempo:.2f} segundos", end=", ")