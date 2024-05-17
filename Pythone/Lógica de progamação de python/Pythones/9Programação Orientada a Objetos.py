#Programação Orientada a Objetos (POO)

# Exemplo de programação orientada a objetos
class Carro:
    def __init__(self, marca, modelo):
    # A chave "def" e o ponto da criação de uma função, logo após voce colocara o nome da função.
        self.marca = marca
        self.modelo = modelo
        # A chave "self" é uma referência ao próprio objeto [a instância da classe]
        # E 'marco' e 'modelo' são parâmetros que são passados quando oobjeto é criado.

    def exibir_informacoes(self):
        print(f"Carro: {self.marca} {self.modelo}")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_informacoes()  # Saída: Carro: Toyota Corolla
