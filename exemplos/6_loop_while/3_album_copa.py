# Variáveis de controle
total_figurinha = 934

# Estruturas de loop e condição
while total_figurinha > 0:
    
    figurinhas_novas = int(input("Quantas figurinhas você quer adicionar? "))

    total_figurinha -= figurinhas_novas
    print(f"⚽ Restam {total_figurinha} figurinhas ")
