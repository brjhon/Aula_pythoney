
somatorio = 0
x = int(input("Digite 1 caso queira somar um número e 0 caso o ver somatório final: "))

while x == 1:
    nimero = int(input("Digite o número que gostaria de somar: "))
    somatorio = somatorio + nimero
    x = int(input("Digite 1 caso queira somar um número e 0 caso ver o somatorio fina: "))

print(somatorio)