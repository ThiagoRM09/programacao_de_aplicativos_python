# 1. Nota Protegida

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota


    @property
    def nota(self):
        return self.__nota

    def definir_nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print("Nota inválida!")

    def situacao(self):
        if self.__nota >= 7 and self.nota <= 10:
            return "Aprovado"
        else:
            return  "Reprovado"

print("\n### Atividade 1 ###\n")

aluno1 = Aluno("Betina", 6.5)
print(aluno1.situacao())
aluno1.definir_nota(15)
aluno1.definir_nota(8)
print(aluno1.nota)
print(aluno1.situacao())

aluno2 = Aluno("Carlos", -2)
print(aluno2.nota)

try:
    aluno2.nota = 10
except:
    print("ERRO!")

# 2 Cofre com senha

class Cofre:
    def __init__(self, senha):
        self.__senha = senha
        self.__itens = []
        self.__aberto = False
        self.__tentativas = 0
        self.__bloqueado = False

    def abrir(self, senha):
        if self.__senha == senha and self.__bloqueado == False:
            self.__aberto = True
            self.__tentativas = 0
            print("Cofre aberto.")
        else:
            self.__tentativas += 1

            if 0 < self.__tentativas <= 3:
                print(f"--- Senha incorreta! Tentativa {self.__tentativas} de 3. ---")

            if self.__tentativas == 3:
                self.__bloqueado = True
                print("Cofre bloqueado!")

    def fechar(self):
        self.__aberto = False
        print("Cofre fechado.")

    def guardar(self, item):
        if self.__aberto:
            self.__itens.append(item)
            print(f"{item} guardado.")
        else:
            print("--- Abra o cofre primeiro! ---")

    def ver_itens(self):
        if self.__aberto:
            print(f"Itens: {self.__itens}")
        else:
            print("--- Não é possível ver itens! Cofre fechado! ---")

print("\n### Atividade 2 ###\n")

cofre = Cofre("1234")
cofre.guardar("Relógio")
cofre.abrir("0000")
cofre.abrir("1234")
cofre.guardar("Relógio")
cofre.ver_itens()
cofre.fechar()

cofre.abrir("1")
cofre.abrir("2")
cofre.abrir("3")

cofre.abrir("1234")

# 3. Controle de estoque

class Produto:
    def __init__(self, nome, preco, quantidade = 0):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    def entrada(self, qtd):
        if qtd > 0:
            self.__quantidade += qtd
            print(f"Entrada de {qtd}! Estoque atual: {self.__quantidade}")
        else:
            print(f"Quantidade inválida! Estoque atual: {self.__quantidade}")

    def saida(self, qtd):
        if self.__quantidade >= qtd > 0:
            self.__quantidade -= qtd
            print(f"Saída de {qtd}! Estoque atual: {self.__quantidade}")
        else:
            print(f"Estoque insuficiente! Disponível: {self.__quantidade}")

    def aplicar_desconto(self, porcentagem):
        if 1 <= porcentagem <= 50:
            self.__preco -= self.__preco * (porcentagem / 100)
            print(f"Desconto aplicado! Novo preço: R$ {self.__preco}")
        else:
            print("Desconto deve ser entre 1% e 50%!")

    def valor_em_estoque(self):
        return f"R$ {self.__preco * self.__quantidade}"

print("\n### Atividade 3 ###\n")

fone = Produto("Fone Bluetooth", 150.0, 10)
fone.saida(3)
fone.saida(20)
fone.entrada(-5)
fone.aplicar_desconto(80)
fone.aplicar_desconto(10)
print(f"R$ {fone.valor_em_estoque()}")

try:
    fone.quantidade = 1000
except:
    print("ERRO!")

fone2 = Produto("Fone Bluetooth", 150.0)
fone2.saida(-3)
fone2.entrada(50)
fone2.aplicar_desconto(80)
fone2.aplicar_desconto(10)
print(f"R$ {fone.valor_em_estoque()}")