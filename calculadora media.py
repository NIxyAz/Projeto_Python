nota_1 = []
nota_2 = []
pim = []
media = []

nome = input("Digite o nome do aluno: ")
nota_1.append(float(input("Digite a primeira nota: ")))
nota_2.append(float(input("Digite a segunda nota: ")))
pim.append(float(input("Digite a nota do PIM: ")))

nota_1[0] = nota_1[0] * (45 / 100)
nota_2[0] = nota_2[0] * (45 / 100)
pim[0] = pim[0] * (10 / 100)
media = (nota_1[0] + nota_2[0] + pim[0])
media = round(media, 2)
print("A média do(a) aluno(a)", nome, "é:", media)


if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else: 
    print("Reprovado")
exit()