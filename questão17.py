Z = int(input("Insira o valor de Z: "))
W = int(input("Insira o valor de W: "))
if W>0 or Z<7:
    x= (5*W+1)/3
    t= 5*Z+2
else:
    x=5*Z+2
    t=(5*W+1)/3
valorY = (7*(x**3)-3*(x**0.5)-8*t)/5*(x+1)
print("O valor de Y é "+str(valorY))