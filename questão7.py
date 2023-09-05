angulo1= float(input("Digite o valor do primeiro angulo: "))
angulo2= float(input("Digite o valor do segundo angulo: "))
angulo3= float(input("Digite o valor do terceiro angulo: "))
soma= angulo1+angulo2+angulo3
if soma != 180:
    print("Os angulos informados nao formam um triangulo.")
else:
    if angulo1<90 and angulo2<90 and angulo3<90:
        print("Os angulos formam um triangulo acutangulo.")
    elif angulo1==90 or angulo2==90 or angulo3==90:
        print("Os angulos formam um triangulo retangulo.")
    elif angulo1>90 or angulo2>90 or angulo3>90:
        print("Os angulos formam um triangulo obtusangulo.")
