idade = input("Digite a sua idade: ")
idade = int(idade)

tem_ingresso = input("Tem ingresso? (sim ou nao): ")
# DESAFIOS 1 - Conversão de implícita de boolean
# DESAFIOS 2 - menu 

if (idade >= 18) or (tem_ingresso == "sim"):
    print("Entrada liberada!")
else:
    print("Você não pode entrar! Tchau")
