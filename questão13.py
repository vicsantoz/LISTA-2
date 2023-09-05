Aço=2.50
Cobre=4
Alum=5
quantAço= int(input("Digite a quantidade de hastes de aço comprados: "))
quantCobre= int(input("Digite a quantidade de hastes de cobre comprados: "))
quantAlum= int(input("Digite a quantidade de hastes de aluminio comprados: "))
valorTotal = quantAço*Aço+quantCobre*Cobre+quantAlum*Alum
quantTotal = quantAço+quantCobre+quantAlum
if quantTotal >= 6:
    desconto = 0
elif 7>= quantTotal >=15:
    desconto=0.10
elif 16>= quantTotal>=20:
    desconto=0.15
else:
    desconto=0.20
valorFinal=valorTotal-valorTotal*desconto
print("O valor final a ser pago sera R$ "+ str(valorFinal)+".") 
