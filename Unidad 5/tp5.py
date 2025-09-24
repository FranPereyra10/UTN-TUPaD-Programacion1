#EJERCICIO 1
#Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

from statistics import mean
lista = []
for i in range (10):
    nota = lista.append(int(input("Ingrese la nota del estudiante: ")))
promedio = mean(lista)
maximo = max(lista)
minimo = min(lista)        

print(lista)
print(f"El promedio de las notas ingresadas es: {promedio}")
print(f"La nota maxima ingresada es: {maximo}")
print(f"La nota minima ingresada es: {minimo}")

#EJERCICIO 2
#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range (5):
    productos.append(input("Ingrese un producto: "))
    productos=sorted(productos)
print(f"Los productos ingresados son: {productos} ")

productos.remove(input("ingrese el producto que desea eliminar: "))
print(productos)

#EJERCICIO 3

#Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
numeros_pares = []
numeros_impares = []

import random

numeros_aleatorios = [random.randint(1,100) for i in range (15)]
print(numeros_aleatorios)

for i in range (15):
    if numeros_aleatorios[i] % 2 == 0:
        numeros_pares.append(numeros_aleatorios[i])
    elif numeros_aleatorios[i] % 2 != 0:
        numeros_impares.append(numeros_aleatorios[i])

print(f"Los numeros pares de la lista son: {numeros_pares}")
print(f"La lista posee {len(numeros_pares)} numeros pares")
print(f"Los numeros impares de la lista son: {numeros_impares}")
print(f"La lista posee {len(numeros_impares)} numeros impares")

#EJERCICIO 4
#Dada una lista con valores repetidos: 1,3,5,3,7,1,9,5,3
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

lista1 = [1,3,5,3,7,1,9,5,3]
lista2 = []
print(f"La lista original es: {lista1}")

for i in lista1:
    if i not in lista2:
        lista2.append(i)
    

print (f"La lista sin elementos repetidos es: {lista2} ")
