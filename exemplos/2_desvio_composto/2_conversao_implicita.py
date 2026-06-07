idade = input("Qual a sua idade:")

if idade:

    # Precisamos fazer a conversão aqui, pois não é possível
    # converter um valor None
    idade = int(idade)

    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
else:
    print("Por favor, digite um valor!")