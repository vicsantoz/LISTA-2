sexo=input("Voce se identifica com o sexo feminino ou masculino? (Digite F ou M) ")
peso= float(input("Insira o seu peso em kg: "))
altura= float(input("Insira a sua altura em cm: "))
idade= int(input("Insira a sua idade: "))
if sexo== "M":
    idealCaloria= 66+ (13.7 * peso) + 5.0 * altura - 6.8* idade
    print("O valor ideal de calorias diarias será " + str(idealCaloria))
elif sexo== "F":
    idealCaloria= 665+ (9.6 * peso) + 1.8* altura - 4.7 * idade
    print("O valor ideal de calorias diarias será " + str(idealCaloria))