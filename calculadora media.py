while True:
    nota = []

    print("=" * 42)
    print("Calculadora de Notas Uniplan 2026")
    print("=" * 42)

    nome = input("Digite o nome completo do aluno(a): ")
    nome_da_diciplina = input("Digite o nome da disciplina: ")
    carga_horaria_semestral = int(input("Digite sua carga horaria: "))
    print("=" * 42)

    #nota 1 [0]
    while True:
        nota_1 = float(input("Digite a primeira nota: "))
        if 0 <= nota_1 <= 10 :
            nota.append(nota_1)
            break
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")

    #nota 2 [1]
    while True:
        nota_2 = float(input("Digite a segunda nota: "))
        if 0 <= nota_2 <= 10:
            nota.append(nota_2)
            break
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")

    #nota do PIM [2]
    while True:
        pim = float(input("Digite a nota do PIM: "))
        if 0 <= pim <= 10:
            nota.append(pim)
            break
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
        
    faltas = int(input("Digite o número de faltas em horas: "))

    print("=" * 42)

    media = (nota[0] * 4 + nota[1] * 4 + nota[2] * 2) / 10
    media = round(media, 2) 
    carga_horaria_total = (faltas / carga_horaria_semestral) * 100
    carga_horaria_total = round(carga_horaria_total, 2)

    print("A média do(a) aluno(a)", nome, "é:", media)
    print("A porcentagem de faltas é:", carga_horaria_total, "%")

    if carga_horaria_total > 25:
        print("Reprovado por faltas")
    elif nota[2] < 5:
        print("Reprovado por pim")
    elif media >= 5 and carga_horaria_total <= 25:
        print("Aprovado")
    else: 
        print("Reprovado")

    print("=" * 42)

    resposta = input("Deseja calcular a nota novamente? (sim/não): ").lower()
    if resposta != 'sim':
        print("Finalizando...")
        break
