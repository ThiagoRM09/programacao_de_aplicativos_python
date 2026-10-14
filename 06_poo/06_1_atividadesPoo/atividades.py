# Atividade: Classes e Objetos, Atributos, Métodos e Construtor

# Atividade 1

class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: Au Au!")

    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Idade: {self.idade}")

cachorro1 = Cachorro("Rex", "Pinscher", 5)
cachorro1.latir()
cachorro1.mostrar_info()

cachorro2 = Cachorro("Xuxinha", "Pinscher", 10)
cachorro2.latir()
cachorro2.mostrar_info()
cachorro2.idade = 12
cachorro2.mostrar_info()

# Atividade 2