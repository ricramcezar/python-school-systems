while True:
    print("\n=== SISTEMA DE BOLETIM SIMPLES ===")

    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        nota1 = float(input("Digite a primeira nota: "))
    
    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.") 
        nota2 = float(input("Digite a segunda nota: "))
    
    nota3 = float(input("Digite a terceira nota: "))
    while nota3 < 0 or nota3 > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        nota3 = float(input("Digite a terceira nota: "))
    
    nota4 = float(input("Digite a quarta nota: "))
    while nota4 < 0 or nota4 > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.") 
        nota4 = float(input("Digite a quarta nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.1f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")
    
    continuar = input("\nDeseja cadastrar outro aluno? [s/n]: ").lower()

    if continuar != "s":
        print("\nSistema encerrado.")
        break