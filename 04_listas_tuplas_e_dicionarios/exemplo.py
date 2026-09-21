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