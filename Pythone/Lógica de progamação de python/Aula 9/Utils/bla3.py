#O "import" e uma biblioteca 
from bla import dobro

#Entrada do usúario
salario_mensal = float(input("Digite  seu salário mensal: R$"))

#Calcula o valor a receber no més do 13°
Valor_recebido = dobro(salario_mensal)

#Imprime o resultado
print(f"Seu salário mensal é R${salario_mensal:.2f}. Você receberá R${salario_mensal:.2f como 13° salário}.")