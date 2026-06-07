# Para algo ser considerado exatamente igual em Python, 
# precisa ter o mesmo valor e o mesmo tipo:

numero = input("Digite um número: ")

if numero == 10:
    print("Os valores são iguais (1)")

if numero == "10":
    print("Os valores são iguais (2)")

numero = int(numero)

if numero == 10:
    print("Os valores são iguais (3)")




