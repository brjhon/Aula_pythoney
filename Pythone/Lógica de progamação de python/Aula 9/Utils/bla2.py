from bla import dobro

#etrada do usúario
limite_atual = float(input("Digite p limite atual do seu cartão de créditos: R$"))

#Calculo o novo limite
novo_limete = dobro(limite_atual)

#Imprime os resultados
print(f"Seu limite atual é R${limite_atual:.2f}. Seu novo limite seria R${novo_limete:.2f}.")

