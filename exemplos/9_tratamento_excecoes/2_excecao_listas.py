produtos_estoque = [
    "mesa", # 0 
    "cadeira", # 1
    "mouse", # 2
    "teclado" # 3
]

try:
    id_produto = int(input("Digite qual produto você quer visualizar: "))
    print(f"PRODUTO: {produtos_estoque[id_produto]}")
except IndexError:
    print("Esse ID não existe")
except ValueError:
    print("Você digitou um índice que não é número")
