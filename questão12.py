sexo=input("Voce se identifica com o sexo feminino ou masculino? (Digite F ou M) ")
idade= int(input("Insira a sua idade: "))
if sexo== "M":
    if idade>=21:
        print("É maior de idade!")
    elif idade<21:
        print("É menor de idade!")
elif sexo=="F":
    if idade>=18:
        print("É maior de idade!")
    elif idade<18:
        print("É menor de idade!")