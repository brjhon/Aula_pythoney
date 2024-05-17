from bla import dobro
#Inportação de uma blibioteca no caso a blibioteca e "bla"

#Entrada do usúario 
valor_emprestado = float(input("Digite o valor que deseja emprestar: R$"))

#Calculo o total a pagar com juros de 100% ao ano
total_pagar = dobro(valor_emprestado)

#Imprime o resultado
print(f"Valor emprestado: R${valor_emprestado:.2f}.  Total a pagar após um ano: R${total_pagar:.2f}.")
