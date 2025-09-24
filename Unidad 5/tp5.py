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

#EJERCICIO5
#EJERCICIO 5
#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada

alumnos = []
add_alumno = 0
for i in range (8):
    alumnos.append(input("Ingrese el nombre de los Alumnos presentes: "))
add_alumno = int(input("Si desea agregar un alumno presione 1. \nSi desea eliminar un alumno Ingrese 2. \n Presione cualquier tecla para continuar."))
if add_alumno == 1:
    alumnos.append(input("Ingrese el Nombre del alumno que desea agregar: "))
elif add_alumno == 2:
    alumnos.remove(input("Ingrese el nombre del alumno que desea eliminar: "))
else:
    pass 


print(f"La lista de alumnos presentes es: {alumnos}")

#EJERCICIO 6
#metodo1
#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).
lista1 = list(range(1,8))
lista2 = []
lista2.append(lista1[6])
lista1.remove(lista1[6])
lista3 = lista2+lista1
print(lista3)

#metodo2 
#lista = list(range(1,8))
#lista2 =[lista[6]]+lista[0:6]
#print(lista2)

#EJERCICIO 7
#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

temperatura_semana = [["Lunes"],["Martes"],["Miercoles"],["Jueves"],["Viernes"],["Sabado"],["Domingo"]]
amplitud=[]
promedio_max = 0
promedio_min = 0


for i in range (7):
    dia = temperatura_semana[i]
   
    temperatura_semana[i].append(input(f"Ingrese la tempera maxima registrada el dia: {dia[0]} : "))
    temperatura_semana[i].append(input(f"Ingrese la temperatura minima registrada el dia: {dia[0]} : "))

print("\nEL cuadro semanal de las temperaturas registradas es el siguiente: ")

for fila in range (len(temperatura_semana)):
    for columna in range (len(temperatura_semana[0])):
        print(temperatura_semana[fila][columna], end=' ')
    print()

for i in range (7):
    temperatura = int(temperatura_semana[i][1])
    promedio_max = promedio_max + temperatura 

print(f"El promedio de las temperaturas maximas registradas es: {(promedio_max/7)} °" )

for i in range (7):
    temperatura = int(temperatura_semana[i][2])
    promedio_min = promedio_min + temperatura 

print(f"El promedio de las temperaturas minimas registradas es: {(promedio_min/7)} °" )

for i in range (7):
     
    amplitud.append([int(temperatura_semana[i][1])-int(temperatura_semana[i][2])])

mayor = amplitud.index(max(amplitud))

print(f"El dia con mayor amplitud termica registrada fue el dia: {temperatura_semana[mayor][0]}")