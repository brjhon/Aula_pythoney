lista = []
clas = int(input("Quantos alunos tem na turma?: "))
quant = 0

for i in range(clas,0,-1):
    name = input(f"Qual e o nome siguinte aluno? {i + 1}: ").lower()#convencional para miniculos antes de adcionar
    lista.append(name)

#Contar quantos "enzo" e "Valentina" estão na lista

contagem_enzo = lista.count("enzo")
contagem_valentina = lista.count("valentina")

#exibir resultados 
print(f"Total de alunos na turma: {clas}")
print(f"Quantidade de alunos chamados enzo: {contagem_enzo}")
print(f"Quantidade de alunos chamados enzo: {contagem_valentina}")
