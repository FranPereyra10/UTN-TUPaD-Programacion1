#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#EJERCICIO1

for i in range (101):
    print (i)

#EJERCICIO2

#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un numero: 10"))
cont = 0

while num != 0:
    num = int(num/10)
    cont += 1 

print (f"La cantidad de digitos del numero ingresado es: {cont}")

#EJERCICIO3