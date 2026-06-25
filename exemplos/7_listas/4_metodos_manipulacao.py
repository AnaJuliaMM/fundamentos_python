jogadores = ["Alisson", "Vini Jr", "Paquetá"]


# 1. Adicionar um novo item no fim da lista: append()
print("\n- Método append()")
jogadores.append("Endrick")
jogadores.append(1)
print(jogadores)


# 2. Adicionar um novo item em uma posição já ocupada: insert()
print("\n- Método insert()")
jogadores.insert(0,"Endrick")
print(jogadores)


# 3. Remove um elemento pelo valor dele
print("\n- Método remove()")
jogadores.remove("Vini Jr")
print(jogadores)

# Gera o erro "x not in list" pois o valor não existe:
# jogadores.remove("aaa")  


# 4. Remove um elemento pelo índice
print("\n- Método pop()")

jogadores.pop() # remove o último
print(jogadores)

jogadores.pop(0) # remove o elemento no índice 0
print(jogadores)


# 5. Contabilizar a ocorrência de um valor (count())
print("\n- Método count()")
jogadores.append("Marquinhos")
jogadores.append("Marquinhos")

print(jogadores.count("Marquinhos")) # 2


# 6. Ordenação
print("\n- Método sort()")
jogadores = ["Alisson", "Vini Jr", "Paquetá"]
codigos = [5, 7,3,4]

# ordem crescente/ alfabética
jogadores.sort()
print(jogadores)

codigos.sort()
print(codigos)

# ordem decrescente / alfabética inversa
jogadores.sort(reverse=True)
print(jogadores)

codigos.sort(reverse=True)
print(codigos)


# 7. Retorna o índice de um elemento (index())
print(jogadores.index("Paquetá")) # 1

# Gera o erro "x not in list" pois o valor não existe:
# print(jogadores.index("AAA"))