distanciaKM = float(input("Digite a distancia percorrida em KM: "))
gasolinaLitros = float(input("Digite a quatidade de gasolina consumida em litros: "))
consumokmL = distanciaKM/gasolinaLitros
print ("O consumo medio do carro é: " + str(consumokmL) + " km/L")
if consumokmL<8:
    print("Venda o carro!")
elif 8<=consumokmL<=12:
    print("Econômico!")
elif consumokmL>12:
    print("Super econômico!")