idade = int(input("Digite sua idade: "))
#O comando funciona "int" funcionara apenas para quando a variavel for usada para números

if idade < 16:
    print("Você ainda não está elegivel para votar.")

elif 18 <= idade < 70:
    print("Seu voto é obrigatório.")

else:
    print("Você está elegivel para votar, mas não é obrigatorio")
    