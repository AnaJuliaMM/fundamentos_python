# >> Variaveis - Declaração e Atribuição

# PORTUGOL:
# caracter nome (criava vazia)
# ...
# nome = "Estou colocando um valor aqui" (Definia um valor)

# PYTHON:

# Criar variáveis (criar e definir o valor):
nome = "Ana Julia"
# Criar variável com valor vazio:
idade = None


# >> Tipagem dinâmica

# 1. O próprio interpretador infere os tipos
nome = "Ana Julia" # STRING ou str (texto)
nome_aspas_simples = 'Ana Julia' # STRING (texto)
idade = 21 # INTEGER ou INT (inteiro)
altura = 1.50 # FLOAT (decimal)
tamanho_camiseta = 'M' # STRING (texto)

print(type(nome))
print(type(nome_aspas_simples))
print(type(idade))
print(type(altura))
print(type(tamanho_camiseta))

# 2. Uma variável pode receber valores de tipos diferentes
print("\n")

nome = "Ana Julia"
print(type(nome))

nome = 21
print(type(nome))