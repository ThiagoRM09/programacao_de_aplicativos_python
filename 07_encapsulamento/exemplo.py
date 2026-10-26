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
ana = Funcionario("Ana", 3000)
print(ana.salario)
ana.dar_aumento(10)
ana.apresentar()

