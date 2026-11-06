print("=== Atividade 1 ===\n")

class Personagem:
    def __init__(self, nome, vida = 100):
        self.nome = nome
        self.__vida = vida

    @property
    def vida(self):
        return self.__vida

    def receber_dano(self, valor):
        if 0 < valor <= self.__vida:
            self.__vida -= valor
            print(f"Dano recebido de {valor} pontos de vida!")
        else:
            print("ERRO ao receber dano!")

    def curar(self, valor):
        if valor > 0 and self.__vida + valor <= 100:
            self.__vida += valor
            print(f"Vida curada em {valor} pontos de vida!")
        else:
            print("ERRO ao curar!")

    def status(self):
        print(f"Nome: {self.nome}\nVida: {self.__vida}")

    def atacar(self):
        return 10

personagem = Personagem("Lorotas")
personagem.receber_dano(120)
personagem.receber_dano(20)
personagem.receber_dano(-20)
personagem.curar(30)
personagem.curar(20)

try:
    personagem.vida = 1000
except:
    print("ERRO ao alterar a vida diretamente!")

class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self):
        return 10 + self.forca

class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self._mana = mana

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = value

    def status_mana(self):
        print(f"Mana atual: {self._mana}")

    def atacar(self):
        if self.mana >= 10:
            self.mana -= 10
            return 25
        else:
            return 5

mago = Mago("Gandalf", 100, 50)
guerreiro = Guerreiro("Zoro", 100, 15)

print("--- mago ---")
mago.receber_dano(120)
mago.receber_dano(20)
mago.receber_dano(-20)
mago.curar(30)
mago.curar(20)

print("--- guerreiro ---")
guerreiro.receber_dano(120)
guerreiro.receber_dano(20)
guerreiro.receber_dano(-20)
guerreiro.curar(30)
guerreiro.curar(20)

print(isinstance(mago, Personagem))
print(isinstance(guerreiro, Personagem))

listaPersonagens = [
    Personagem("Homem-Aranha"),
    Guerreiro("Deku", 100, 15),
    Mago("Bruxa", 100, 50)
]

for personagem in listaPersonagens:
    print(f"Nome: {personagem.nome}\nAtaque: {personagem.atacar()}")

print("\n=== Atividade 2 ===")

class Produto:
    def __init__(self, nome, preco, estoque = 0):
        self.nome = nome,
        self.preco = preco
        self.__estoque = estoque

    @property
    def estoque(self):
        return self.__estoque

    def repor(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
            print(f"Reposição de {quantidade} unidades!")
        else:
            print(f"Não foi possível repor a quantidade de {quantidade}!")

    def vender(self, quantidade):
        if 0 < quantidade <= self.__estoque:
            self.__estoque -= quantidade
            print(f"Venda de {quantidade} unidades!")
            print(f"Estoque atual: {self.__estoque} unidades!")
        else:
            print(f"Não foi possível vender a quantidade de {quantidade}!")

    def informacoes(self):
        print(f"Nome: {self.nome} \nPreço: R$ {self.preco}\nEstoque: {self.__estoque}")

    def preco_final(self):
        return self.preco * 1.1

produto = Produto("Garrafa", 19.90, 100)
produto.repor(10)
produto.repor(-10)
produto.vender(120)
produto.vender(-120)
produto.vender(110)
produto.informacoes()

try:
    produto.estoque = 10
except:
    print("ERRO ao alterar o estoque diretamente!")

class ELetronico(Produto):
    def __init__(self, nome, preco, estoque, garantia):
        super().__init__(nome, preco, estoque)
        self.garantia = garantia

    def preco_final(self):
        return self.preco * 1.2 + 5 * self.garantia

class Alimento(Produto):
    def __init__(self, nome, preco, estoque, validade):
        super().__init__(nome, preco, estoque)
        self.validade = validade

    def preco_final(self):
        return self.preco * 1.05

    @property
    def validade(self):
        return self.validade

    @validade.setter
    def validade(self, value):
        self._validade = value

eletronico = ELetronico("Notebook", 4000, 10, 12)
alimento = Alimento("Arroz", 10, 10, "2026-11-10")

print("=== Eletronico ===")
eletronico.repor(10)
eletronico.repor(-10)
eletronico.vender(120)
eletronico.vender(-120)
eletronico.vender(10)
eletronico.informacoes()
eletronico.preco_final()

print("=== Alimento ===")
alimento.repor(10)
alimento.repor(-10)
alimento.vender(120)
alimento.vender(-120)
alimento.vender(5)
alimento.informacoes()
alimento.preco_final()

print(isinstance(eletronico, Produto))
print(isinstance(alimento, Produto))

listaProdutos = [
    Produto("Caneta", 2, 10),
    ELetronico("Celular", 1500, 5, 12),
    Alimento("Macarrão", 5, 20, "2026-12-10")
]

for produto in listaProdutos:
    print(f"Nome: {produto.nome}\nPreço final: R$ {produto.preco_final()}")

# Atividade 3
print("\n ===== Atividade 3 =====")

class Veiculo:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
        self.__quilometragem = 0

    def quilometragem(self):
        return self.__quilometragem

    def registrar_viagem(self, km):
        if km > 0:
            self.__quilometragem += km
            print(f"{km}km adicionados à quilometragem!")
        else:
            print(f"Não foi possível registrar {km}km à quilometragem!")

    def detalhes(self):
        print(f"Modelo: {self.modelo}\nPlaca: {self.placa}\nQuilometragem: {self.__quilometragem}")

    def valor_diaria(self):
        return 100

    def alugar(self, dias):
        if self.__quilometragem > 50000:
            print(f"Valor total do aluguel: R$ {(self.valor_diaria() * dias) * 0.85}")
        else:
            print(f"Valor total do aluguel: R$ {self.valor_diaria() * dias}")

print("\n ===== Veículo =====")
veiculo = Veiculo("Porsche 911", "1234FD12")
veiculo.registrar_viagem(500000)
veiculo.registrar_viagem(-50)
veiculo.detalhes()
veiculo.quilometragem()
veiculo.alugar(10)

try:
    veiculo.__quilometragem = 10
except:
    print("Não foi possível alterar a quilometragem diretamente!")


class Carro(Veiculo):
    def __init__(self, modelo, placa, portas):
        super().__init__(modelo, placa)

        if portas == 4 or portas == 2:
            self.portas = portas
        else:
            print("Número de portas INVÁLIDO!")

    def detalhes(self):
        print(f"Modelo: {self.modelo}\nPlaca: {self.placa}\nQuilometragem: {self.quilometragem()}\nPortas: {self.portas}")

    def valor_diaria(self):
        if self.portas == 4:
            return 170
        else:
            return 150

class Moto(Veiculo):
    def __init__(self, modelo, placa, cilindradas):
        super().__init__(modelo, placa)

        if cilindradas > 0:
            self.cilindradas = cilindradas
        else:
            print("Número de cilindradas INVÁLIDO!")

    def cilindradas(self):
        return self.cilindradas

    def detalhes(self):
        print(f"Modelo: {self.modelo}\nPlaca: {self.placa}\nQuilometragem: {self.quilometragem()}\nCilindradas: {self.cilindradas}")

    def valor_diaria(self):
        if self.cilindradas > 300:
            return 110
        else:
            return 80

print("\n ===== Carro =====")
carro = Carro("Tiggo 5", "1234FD11", 4)
carro.registrar_viagem(50)
carro.registrar_viagem(-50)
carro.detalhes()
carro.quilometragem()

try:
    carro.__quilometragem = 10
except:
    print("Não foi possível alterar a quilometragem diretamente!")

print("\n ===== Moto =====")
moto = Moto("X6", "1111AA11", 160)
moto.registrar_viagem(50)
moto.registrar_viagem(-50)
moto.detalhes()
moto.quilometragem()

try:
    moto.__quilometragem = 10
except:
    print("Não foi possível alterar a quilometragem diretamente!")

print(isinstance(moto, Veiculo))
print(isinstance(carro, Veiculo))

veiculos = [
    Veiculo("Porsche 911", "1234FD12"),
    Moto("X4", "1111AA22", 301),
    Carro("Tiggo 7", "1234FD77", 4)
]

print("\n===== Lista =====")
for veiculo in veiculos:
    print("\n--- Veículo ---\n")
    veiculo.detalhes()
    print(veiculo.valor_diaria())



