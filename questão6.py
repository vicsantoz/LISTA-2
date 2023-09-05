media=float(input("Digite a media do aluno: "))
faltas=int(input("Digite o numero de faltas do aluno: "))
if(media>=7 and faltas<=32):
    print("O aluno esta aprovado.")
elif(media<7 and faltas<=32):
    print("O aluno esta reprovado por media.")
elif(media>=7 and faltas>32):
    print("O aluno esta reprovado por faltas.")
else:
    print("O aluno esta reprovado por faltas e por media.")