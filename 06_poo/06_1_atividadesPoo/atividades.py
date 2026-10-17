# Atividade: Classes e Objetos, Atributos, Métodos e Construtor

# Atividade 1
print("\n=== Atividade 1 ===\n")

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
print("\n=== Atividade 2 ===\n")

class Livro:
    def __init__(self, titulo, autor, totalPaginas):
        self.titulo = titulo
        self.autor = autor
        self.totalPaginas = totalPaginas
        self.totalDePaginasLidas = 0
        self.paginasLidas = 0

    def ler(self, paginasLidas):
        if self.totalDePaginasLidas <= self.totalPaginas:
            self.totalDePaginasLidas += paginasLidas

    def porcentagem_lida(self):
        return self.totalDePaginasLidas / self.totalPaginas * 100

    def paginas_restantes(self):
        return self.totalPaginas - self.totalDePaginasLidas

    def terminou(self):
        if self.totalDePaginasLidas == self.totalPaginas:
            return True
        else:
            return False

livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro2 = Livro("Incidente em Antares", "Erico Verissimo", 550)

contador1 = 1
contador2 = 1

while contador1 < 5:
    livro1.ler(64)
    print(livro1.porcentagem_lida())
    print(livro1.paginas_restantes())
    print(livro1.terminou())
    contador1 += 1

while contador2 < 12:
    livro2.ler(50)
    print(livro2.porcentagem_lida())
    print(livro2.paginas_restantes())
    print(livro2.terminou())
    contador2 += 1

# Atividade 3
print("\n=== Atividade 3 ===\n")

class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Saldo atual: R$ {self.saldo}"
        else:
            return f"Não é possível realizar o deposito!"

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saldo atual: R$ {self.saldo}"
        else:
            return f"Saldo insuficiente!"

    def extrato(self):
        print(f"Titular da conta: {self.titular}")
        print(f"Saldo da conta: R$ {self.saldo}")

contaBancaria1 = ContaBancaria("Lacerda")
print(contaBancaria1.depositar(-100))
print(contaBancaria1.depositar(100))
print(contaBancaria1.sacar(150))
print(contaBancaria1.sacar(60))
print(contaBancaria1.sacar(40))
contaBancaria1.extrato()

contaBancaria2 = ContaBancaria("Marcos", 500)
print(contaBancaria2.depositar(-100))
print(contaBancaria2.depositar(100))
print(contaBancaria2.sacar(150))
print(contaBancaria2.sacar(60))
print(contaBancaria2.sacar(40))
contaBancaria2.extrato()

# Atividade 4
print("\n=== Atividade 4 ===\n")

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.nivel = 1

    def receber_dano(self, valor):
        if 0 < valor <= self.vida:
            self.vida -= valor
            print(f"Dano de {valor} recebido!")
            print(f"Vida atual: {self.vida}")

            if self.vida == 0:
                print(f"{self.nome} foi derrotado!")
        else:
            print("Dano não recebido!")

    def curar(self, valor):
        if (valor > 0) and (valor + self.vida) <= 100:
            self.vida += valor
            print(f"Cura de {valor} recebida!")
            print(f"Vida atual: {self.vida}")
        else:
            print(f"Cura não recebida!")

    def subir_nivel(self):
        self.nivel += 1
        self.vida = 100

    def status(self):
        return (f"\nNome: {self.nome} "
                f"\nClasse: {self.classe}"
                f"\nNível: {self.nivel}"
                f"\nVida: {self.vida}")

personagem1 = Personagem("Naruto", "Ninja")
personagem1.receber_dano(70)
personagem1.curar(71)
print(personagem1.vida)
personagem1.subir_nivel()
print(personagem1.vida)
print(personagem1.nivel)
print(personagem1.status())

personagem2 = Personagem("Luffy", "Pirata")
personagem2.receber_dano(70)
personagem2.receber_dano(31)
personagem2.receber_dano(30)

# Atividade 5
print("\n=== Atividade 5 ===\n")

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)
        print("Produto adicionado!")

    def total(self):
        somaSubTotais = 0

        for item in self.itens:
            somaSubTotais += item.subtotal()

        return somaSubTotais

    def mostrar(self):
        for item in self.itens:
            print("\n=== PRODUTO ===")
            print(f"Nome: {item.nome}")
            print(f"Preço: R$ {item.preco}")
            print(f"Quantidade: {item.quantidade}")
            print(f"Subtotal: R$ {item.subtotal()}")

        print(f"\nTOTAL DA COMPRA: R$ {self.total()}")

carrinho = Carrinho()

produto1 = Produto("Caneta", 2, 2)
carrinho.adicionar(produto1)

produto2 = Produto("Mouse", 50, 2)
carrinho.adicionar(produto2)

produto3 = Produto("Teclado", 100, 1)
carrinho.adicionar(produto3)

produto4 = Produto("Mousepad", 20, 1)
carrinho.adicionar(produto4)

print(carrinho.total())
carrinho.mostrar()