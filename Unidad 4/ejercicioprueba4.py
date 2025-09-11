# Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0
num = int(input("Ingrese cero para salir \nIngrese un numero: "))
while num != 0:
    suma += num
    num = int(input("Ingrese cero para salir \nIngrese un numero: "))

print ("La suma total de los numeros ingresados es: ",suma)