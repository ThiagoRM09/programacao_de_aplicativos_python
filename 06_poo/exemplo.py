# 1. Classe: o modelo (planta)

class Celular:
    def __init__(self, marca, modelo, cor, nivelBateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.nivelBateria = nivelBateria
        self.ligado = False

# 2. Métodos: os comportamentos do objeto

    def toString(self):
        print("\n=== INFORMAÇÕES DO CELULAR ===")
        print(f"\nMarca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Nível de Bateria: {self.nivelBateria}")
        print(f"Ligado: {self.ligado}")

    def ligar(self):
        if not self.ligado:
            if self.nivelBateria > 0:
                self.ligado = True
                print("Celular LIGADO!")
            else:
                print("Não foi possível LIGAR um celular COM NÍVEL DE BATERIA ZERADO!")
        else:
            print("Não foi possível LIGAR um celular JÁ LIGADO!")

    def desligar(self):
        if self.ligado:
            if self.nivelBateria > 0:
                self.ligado = False
                print("Celular DESLIGADO!")
            else:
                print("Não foi possível DESLIGAR um celular COM NÍVEL DE BATERIA ZERADO!")
        else:
            print("Não foi possível DESLIGAR um celular JÁ DESLIGADO!")

# 3. Objetos: Criados a partir da classe (as casas)

celular1 = Celular("Samsung", "A57", "Preto", 0)
celular2 = Celular("Apple", "Iphone 18 Pro Max", "Bordô")

# 4. Acessando e alterando atributos
#usamos objeto.atributo

print(celular1.nivelBateria)
print(celular2.marca)
print(celular2.nivelBateria)

# 5. Acessando métodos

celular1.toString()
celular1.desligar()