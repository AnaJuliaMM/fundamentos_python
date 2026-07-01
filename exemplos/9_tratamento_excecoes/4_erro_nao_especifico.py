produtos_estoque = [
    "mesa", # 0 
    "cadeira", # 1
    "mouse", # 2
    "teclado" # 3
]

try:
    id_produto = int(input("Digite qual produto você quer visualizar: "))
    print(f"PRODUTO: {produtos_estoque[id_produto]}")
except Exception as e:
    print(f"Houve algum erro no sistema: {e}")
# except:
#     print(f"Houve algum erro no sistema")
