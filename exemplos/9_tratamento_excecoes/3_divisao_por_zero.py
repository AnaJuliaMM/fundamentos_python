try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    divisao = numero1 / numero2

    print(f"O resultado é {divisao}")
except ValueError as e:
    print("Você digitou um valor que não é número!")
except ZeroDivisionError:
    print("Não é possível dividir por 0")