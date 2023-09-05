tipoConsu=input("Informe o tipo de consumidor (Digite 'I' para industrial, 'C' para comercial e 'R' para residencial): ")
consumo= float(input("Insira a quantidade de energia consumida: "))
if tipoConsu == "I" :
    valorPago = 0.68*consumo+34
elif tipoConsu == "C" :
    valorPago = 0.37*consumo+45
elif tipoConsu == "R" :
    valorPago = 0.77*consumo-22
print("O valor final a ser pago será R$ "+str(valorPago)) 