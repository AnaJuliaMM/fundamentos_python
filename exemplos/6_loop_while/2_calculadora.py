# Declarar variavel de controle
deseja_sair = 'N'

# Construir loop e a condicao
while deseja_sair != 'S':

    print("\nSeja bem vindo a sua calculadora!")

    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))

    print("\nO que você gostaria de fazer?")
    print("A - Somar os números")
    print("B - Subtrair os números")
    print("C - Multiplicar os números")
    print("D - Dividir os números")
    opcao = input("OPÇÃO SELECIONADA: ")

    match (opcao):
        case "A":
            print(f"Resultado: {numero1+numero2}")
        case "B":
            print(f"Resultado: {numero1-numero2}")
        case "C":
            print(f"Resultado: {numero1*numero2}")
        case "D":
            print(f"Resultado: {numero1/numero2}")

    # Modificar variável de controle
    deseja_sair = input("\nDeseja sair (S ou N)?: ")
