print("Qual turma você pertence?")
print("1 - Turma A")
print("2 - Turma B")
print("3 - Turma C")
turma = int(input("Digite sua opção: "))

match turma: 
    case 1:
        print("Você pertence a turma A")
    case 2:
        print("Você pertence a turma B")
    case 3:
        print("Você pertence a turma C")
    case _:
        print("Digite uma opção válida")



