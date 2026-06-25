# 1. Criação de listas
notas = [] # lista vazia
jogadores = [
    "Alisson",
    "Vini Jr.", 
    "Paquetá", 
    "Raphinha",
    "Casemiro",
    "Endrick"
]


# 2. Comprimento da lista (qtdl. de itens)
# len(nome_lista)
print("\n1- Comprimento das listas")
print(len(notas)) #0
print(len(jogadores)) # 6


# 3. Mostrar o conteudo inteiro de uma vez
print("\n2- Mostrar o conteudo inteiro de uma vez")
print(notas)
print(jogadores)


# 4. Acessando itens específicos
print("\n3- Buscar elemento pelo indice")
print(jogadores[0]) # Alisson
print(jogadores[1]) # Vini Jr.
print(jogadores[-1]) # Endrick (ultimo)

# Formas diferentes de acessar o último elemento
print(jogadores[-1])
print(jogadores[5])
print(jogadores[len(jogadores)-1]) 

# Acessando um elemento inexistente (erro)
# print(jogadores[6])
print(notas[10])