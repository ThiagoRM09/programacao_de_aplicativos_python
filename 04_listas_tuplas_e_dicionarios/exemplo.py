# Listas, Tuplas e Dicionários

# 1. Listas

nomes = ['Ana', 'Betina', 'Clara']
print(nomes)

# 1.1 Acessando os elementos da lista

print(nomes[0])
print(nomes[1])
print(nomes[-1]) # -1 para acessar o último índice da lista

# 1.2 Alterando elemento na lista

nomes[0] = 'Pedro'
print(nomes)

# 1.3 Adicionando elemento na lista

# append() -> adiciona um elemento no final da lista

nomes.append('Daniel')
print(nomes)

# insert() -> adiciona um elemento numa posição a escolher

nomes.insert(0, "JM")
print(nomes)

# remove() -> remove um elemento pelo um valor

nomes.remove('JM')
print(nomes)

# pop() -> remove um elemento pelo índice

nomes.pop() # -> remove o último elemento da lista
print(nomes)

# Tamanho da lista

# len() informa a quantidade de elementos
print(len(nomes))

# Percorrendo uma lista
for nome in nomes:
    print(nome)

# Verificando se um elemento existe
if "João" in nomes:
    print("João está na lista!")
else:
    print("João não está na lista!")

# Lista com Diferentes tipos de dados
dados = ["João", 18, 1.75, True]
print(dados)

# Lista de números
notas = [7.5, 8, 6.5, 9]
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media:.1f}")


# Tuplas
# Tuplas são semelhantes às listas
# A principal diferença é que tuplas não podem
# ser alteradas depois de criadas

coordenadas = (10,20)
print(coordenadas)

# Acessando os elementos
print(coordenadas[0])
print(coordenadas[1])


# Dicionários
# Armazena informações no formato:
# chave: valor

aluno = {
    "nome": "Thigas",
    "idade": 17,
    "nota": 10
}

print(aluno)

# Acessando os valores
print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

# Alterando os valores

aluno["nota"] = 9
print(aluno)