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
