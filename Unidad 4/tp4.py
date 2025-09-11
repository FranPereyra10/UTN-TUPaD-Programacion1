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
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
#Le pedimos al usuario que ingrese dos valores de inicio y fin
print ("Ingrese dos valores: ")
num1 = int(input("Numero1: ")) 
num2 = int(input("Numero2: "))
sumatoria = 0
#planteamos un condicional para separar los casos donde el primer numero sea mayor y otro para el caso que sea menor que el segundo
if num1 < num2:
    for i in range (num1+1,num2):
        num = i
        sumatoria += num
elif num1 > num2:
    for i in range (num1-1,num2,-1):
        num = i
        sumatoria += num
print (sumatoria)


#EJERCICIO4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0
num = int(input("Ingrese cero para salir \nIngrese un numero: "))
while num != 0:
    suma += num
    num = int(input("Ingrese cero para salir \nIngrese un numero: "))

print ("La suma total de los numeros ingresados es: ",suma)

#EJERCICIO5

#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
num = int(input("Ingrese un numero: "))
import random
num_aleat = random.randint(0,9)
cont = 1
while num != num_aleat:
    cont += 1  
    num = int(input(("Intenta otra vez: ")))

print(f"El numero a adivinar era: {num_aleat}")
print(f"Usted a ocupado {cont}, intentos ")

#EJERCICIO6

#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range (100,-1,-1):
    if i % 2 == 0:
        print (i)

#EJERCICIO7
#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero positivo: "))
suma = 0
for i in range (0,num+1,1):
    suma += i

print(f"La suma total de los numeros comprendidos entre cero y el numero ingresado es: {suma}")