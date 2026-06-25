# 1. Formatar as palavras dentro da string
nome = "Ana JUlIA"
print(nome.lower()) # caixa baixa
print(nome.upper()) # CAIXA ALTA
print(nome.capitalize()) # Primeira letra em maiusculo

# 2. Limpeza de espaços
nome = " Ana Julia "
print(nome)
print(nome.strip())

# 3. Não podemos alterar uma lista, mas podemos criar uma nova versão
nome = "Ana-julia"
print(nome)

com_espace = nome.replace("-", " ")
print(com_espace)

sem_espaco = nome.replace("-", "")
print(sem_espaco)


# 4. Separa as palavras baseado em um caracter e cria uma lista
# com essas palavras
nome = "Ana-julia"
print(nome.split())
print(nome.split("-"))

nome = "Ana julia"
print(nome.split(" "))


# 5. Tranforma uma lista em string
jogadores = [
    "Casemiro",
    "Vini Jr.",
    "Endrick",
    "Alisson"
]
print(jogadores)

jogadores = "_".join(jogadores)
print(jogadores)
