jogadores = ["Alisson", "Vini Jr", "Paquetá"]

# 1. Método append()
print("\n1 - Método append()")
jogadores.append("Endrick")
jogadores.append(1)

print(jogadores)

# 2. Remove um elemento pelo valor exato
print("\n2 - Método remove()")
jogadores.remove("Vini Jr")
print(jogadores)
# Tentando algo que não existe
jogadores.remove(1)
print(jogadores)


# 3. Remover pelo índice
print("\n3 - Método pop()")

jogadores = ["Alisson", "Vini Jr", "Paquetá"]
jogadores.pop()
print(jogadores)

jogadores.pop(0)
print(jogadores)


# 4. Ordenação
print("\n4 - Método sort()")
jogadores = ["Alisson", "Vini Jr", "Paquetá"]
codigos = [5, 7,3,4]

# ordem crescente
jogadores.sort()
print(jogadores)

codigos.sort()
print(codigos)

# ordem decrescente
jogadores.sort(reverse=True)
print(jogadores)

codigos.sort(reverse=True)
print(codigos)


# 5. Contar o número de ocorrência com count()
print("\n5 - Método count()")

clientes = ["Ana Julia", "Ana Julia", "Paulo"]
quantidade = clientes.count("Ana Julia")
print(quantidade) # 2



clientes = ["Ana", "João", "Albert"]
clientes.insert(2, "Ana")
print(clientes) # ['Ana', 'João', 'Ana', 'Albert']