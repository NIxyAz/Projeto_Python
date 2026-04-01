nota = []

nome = input("Digite o nome do aluno: ")
nome_da_diciplina = input("Digite o nome da disciplina: ")
carga_horaria = int(input("Digite a carga horária da disciplina: "))

#nota 1 
while True:
    nota_1 = float(input("Digite a primeira nota: "))
    if 0 <= nota_1 <= 10:
        nota.append(nota_1)
        break
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

#nota 2
while True:
    nota_2 = float(input("Digite a segunda nota: "))
    if 0 <= nota_2 <= 10:
        nota.append(nota_2)
        break
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

#nota do PIM
while True:
    pim = float(input("Digite a nota do PIM: "))
    if 0 <= pim <= 10:
        nota.append(pim)
        break
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        
faltas = int(input("Digite o número de faltas: "))

media = (nota[0] * 4 + nota[1] * 4 + nota[2] * 2) / 10
media = round(media, 2) 

print("A média do(a) aluno(a)", nome, "é:", media)

if faltas > 30:
    print("Reprovado por faltas")
elif nota[2] < 5:
    print("Reprovado por pim")
elif media >= 5 and faltas <= 30:
    print("Aprovado")
else: 
    print("Reprovado")
exit()
