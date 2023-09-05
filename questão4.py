num1=int(input("Insira o primeiro numero: "))
num2=int(input("Insira o segundo numero: "))
num3=int(input("Insira o tereciro numero: "))
if(num1>num2):
    if(num1>num3):
        print("O numero " + str(num1) + " é o maior numero.")
    else:
        print("O numero " + str(num3) + " é o maior numero.")
elif(num1<num2):
     if(num2>num3):
        print("O numero " + str(num2) + " é o maior numero.")
     else:
        print ("O numero " + str(num3) + " é o maior numero.")