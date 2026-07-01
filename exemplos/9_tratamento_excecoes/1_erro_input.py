try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    soma = numero1 + numero2

    print(f"O resultado é {soma}")
except ValueError as e:
    print(f"Você digitou um valor que não é número!")
    print(e)



