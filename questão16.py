numero=int(input("Digite um numero inteiro de tres digitos: "))
primeiroDigito = numero//100
auxNumero = numero%100
segundoDigito = auxNumero//10
terceiroDigito = auxNumero%10
novoNumero= primeiroDigito + terceiroDigito + segundoDigito
print("A soma dos numeros é igual a " + str(novoNumero))
if novoNumero%16==0 and novoNumero%4==0:
    print("O novo número é divisor de 16 e múltiplo de 4 ao mesmo tempo.")
else:
    print("O novo número nao é divisor de 16 e múltiplo de 4 ao mesmo tempo.")