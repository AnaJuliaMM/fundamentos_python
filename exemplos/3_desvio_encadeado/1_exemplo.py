media = float(input("Digite a média: "))

if media >= 9:
    print("Aluno excelente")
elif media >= 7:
    print("Aluno aprovado")
elif media >= 5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")