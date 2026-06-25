# 1. Uma string sempre começa e termina com " ou '
nome = "Ana Julia"
nome = 'Ana Julia'


# 2. Problema das aspas dentro de aspas
frase = "Meu nome é 'Ana Julia'"
frase = 'Meu nome é "Ana Julia"'


# 2. Caracter especial (\)
print("Linha 1\nLinha 2\nLinha 3") # quebra de linhas
print("Linha 1 Linha 2\n\tLinha 3") # insere uma tabulacao (identacao) na exibição
print("Barra invertida \\")


# 3. Aspas triplas: string de múltiplas linhas, não 
# necessita inserir \n ou \t pois já insere automaticamente de forma invisível
print("""
    Lista 1
    lista 2
    Lista 3
""")


# 4. Slicing/Fatiamento: extrair um subtring
nomes = ["Livia", "Rubens", "Gabriel", "Gustavo"]
sublista = nomes[1:]
print(sublista)

nome = "Livia"
subtring = nome[1:]
print(subtring)

inverter = nome[::-1]
print(inverter)

# 5. String são imutáveis
nomes = ["Livia", "Rubens", "Gabriel", "Gustavo"]
nomes[1] = "Rubens Garcia"
print(nomes)

nome = "Livia"
nome[1] = "T" # erro: 'str' object does not support item assignment
print(nome)