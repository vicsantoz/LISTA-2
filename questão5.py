nomeAluno= input("Digite o nome do aluno: ")
prova1= int(input("insira a cota da prova 1: "))
prova2= int(input("insira a cota da prova 2: "))
media= prova1+prova2/2
if(0<media<=5):
    print("O aluno " + nomeAluno + "esta reprovado")
elif(5<media<=7):
    print("O aluno " + nomeAluno + "esta de recuperação")
else:
    print("O aluno " + nomeAluno + "esta aprovado")