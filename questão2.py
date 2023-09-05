disCar1= float(input("Insira a distancia percorrida pelo primeiro carro: "))
tempCar1= float(input("Insira o tempo levado pelo primeiro carro: "))
disCar2= float(input("Insira a distancia percorrida pelo segundo carro: "))
tempCar2= float(input("Insira o tempo levado pelo segundo carro: "))
velocMed1= disCar1/tempCar1
velocMed2= disCar2/tempCar2 
if(velocMed1>velocMed2):
    print ("O primeiro carro teve a maior velocidade media.")
elif(velocMed1<velocMed2):
        print ("O segundo carro teve a maior velocidade media.")
else: 
      print("A velocidade media dos carros foi igual")