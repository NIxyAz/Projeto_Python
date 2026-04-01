nota = []

nome = input("Digite o nome do aluno: ")
nome_da_diciplina = input("Digite o nome da disciplina: ")
carga_horaria_semestral = 300
print("A carga horária semestral da disciplina é de", carga_horaria_semestral, "horas presenciais.")

#nota 1 [0]
while True:
    nota_1 = float(input("Digite a primeira nota: "))
    if 0 <= nota_1 <= 10:
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

media = (nota[0] * 4 + nota[1] * 4 + nota[2] * 2) / 10
media = round(media, 2) 
carga_horaria_total = (faltas / carga_horaria_semestral) * 100

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
exit()
