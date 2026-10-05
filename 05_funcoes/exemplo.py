# Funções

# Uma função é um bloco de código criado para realizar uma determinada tarefa

# Ela permite organizar e reutilizar o código

# 1. Criando uma função

# Utilizar a palavra def para uma função

def saudacao():
    print("Olá, seja bem vindo!")

saudacao()

# 2. Função com parâmetro

nome = "Thiago"

def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("THI")
saudacao(nome)

# 3. Mais de um parâmetro

def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar("Thiago", 17)

# 4. Função com cálculo

def somar(num1, num2):
    print(f"A soma de {num1} + {num2} é: {num1 + num2}")

somar(10, 5)

# 5. Retornando um valor

def somar(numero1, numero2):
    return f"A soma de {numero1} + {numero2} é: {numero1 + numero2}"

mensagemRetornada: str = somar(12, 12)
print(mensagemRetornada)

# 6. Função com condição

def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

retorno = verificarIdade(17)
print(retorno)

# 7. Parâmetro com valor padrão

def saudacao(nome="Thiago"):
    print(f"Olá, {nome}")

saudacao()

# 8. Vários parâmetros

def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

print(calcularMedia(8, 7, 9))

# 9. Funções para organizar um programa

def cadastrarProduto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    return nome, preco

def exibirProduto(nome, preco):
    print("\n ==== PRODUTO ====")
    print(f"Nome: {nome}")
    print(f"Preço: {preco}")

nome, preco = cadastrarProduto()
exibirProduto(nome, preco)