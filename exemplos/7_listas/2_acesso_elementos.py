alunos = [
    "Rubens", "Gabriel", 
    "Yago", "Lucas", 
    "Lana", "Lívia"
] 

# 1. For each para automatizar o acesso dos itens:
print("\n1. FOR EACH: ")
for aluno in alunos:
    print(aluno)


# 2. Fatiamento: extrair partes de uma lista sem modificar a original
# lista[inicio:fim:passo]
print("\n2. SLICING: ")


# Exibir os elementos no índice 0, 1 e 2:
print(alunos[:3])

# Exibir os elementos no índice 4 em distante:
print(alunos[4:])

# Exibir os elementos no índice 3, 4 e 5:
print(alunos[3:6])

# Exibir os elementos no índice 1, 3 e 5:
print(alunos[1:6:2])