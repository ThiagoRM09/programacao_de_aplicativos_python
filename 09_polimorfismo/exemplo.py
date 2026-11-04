# 1. Encapsulamento

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"salario: R$ {self.__salario:.2f}")

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido!")
            return
        else:
            self.__salario = self.__salario * (1 + (porcentagem / 100))
            print(f"{self.nome} recebeu {porcentagem}% de aumento.")

    def bonus(self):
        return self.salario * 0.1

ana = Funcionario("Ana", 3000)
print(ana.salario)
ana.dar_aumento(10)
ana.apresentar()

# 2. Herança
print("\n--- Herança ---\n")

class Gerente(Funcionario):

    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def mostrar_equipe(self):
        print(f"{self.nome} gerencia {self.equipe} pessoas.")

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

fulano = Gerente("Fulano", 8000, 5)
caio = Estagiario("Caio", 1500, "Análise de Sistemas")

fulano.apresentar()
caio.apresentar()
caio.dar_aumento(5)
caio.apresentar()

# 3. Polimorfismo

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def bonus(self):
        return self.salario * 0.2 + self.equipe * 100

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def bonus(self):
        return 200

print("\n ===== Polimorfismo =====")

equipe = [
    Funcionario("Ana", 3000),
    Gerente("Bruno", 8000, 5),
    Estagiario("Caio", 1500, "Análise de Sistemas")
]

for funcionario in equipe:
    print(f"{funcionario.nome}: R$ {funcionario.bonus()}")


