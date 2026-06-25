jogadores = [
    "Alisson",
    "Vini Jr.", 
    "Paquetá", 
    "Raphinha", 
    "Casemiro",
    "Endrick" 
]


# 1. For each (percorrer todos os elementos da lista)
for jogador in jogadores:
    print(f"O jogador atual é {jogador}")


# 2. Fatiamento (Slicing)
# nome_lista[incio:fim:incremento] (não inclui o item no índice 3)

# Exibir os elementos de índice 0, 1 e 2
print(jogadores[:3])

# Exibir os elementos de indice 4 e 5
print(jogadores[4:6])

# Exibir os elementos de indíce 3 em diante (até o último)
print(jogadores[3:])

# Exibir os elementos de indíce 1 até 5 pulando de 2 em 2
print(jogadores[1:6:2])
