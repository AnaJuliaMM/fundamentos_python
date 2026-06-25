# DESAFIO 1

# Criar a lista vazia
tarefas = []

# Adicionar tarefas
tarefas.append("Tomar café da manhã")
tarefas.append("Responder mensagens no Whatsapp")
tarefas.append("Estudar listas em Python")

# Remover a segunda tarefa
tarefas.pop(1)

# Ordenar a lista
tarefas.sort()

# Exibir
print(tarefas)


# ---------------------------------------------------------------------------------
# DESAFIO 2

fila = ['João', 'Maria']

fila.append("José")
fila.append("Sônia")
fila.insert(0, "Alice")

print(fila)


# ---------------------------------------------------------------------------------
# DESAFIO 3

numeros = [10, 20, 30, 20, 40, 20, 50]

quantidade = numeros.count(20)
print(f"O número 20 aparece {quantidade} vezes")

indice = numeros.index(20)
print(f"O primeira ocorrência está na índice {indice}")
