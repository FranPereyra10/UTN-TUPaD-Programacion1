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
#último pasa a ser el primero).
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

#EJERCICIO 8
#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

listado = [[],[],[]]

for i in range (3):
    listado[i].append(input("Ingrese el nombre de la materia: "))

for i in range(5):
    listado[0].append(int(input(f"Ingrese la nota del {i+1}° estudiante en {listado[0][0]}:")))
    listado[1].append(int(input(f"Ingrese la nota del {i+1}° estudiante en {listado[1][0]}:")))
    listado[2].append(int(input(f"Ingrese la nota del {i+1}° estudiante en {listado[2][0]}:")))

for fila in range (len(listado)):
    for columna in range (len(listado[0])):
        print(listado[fila] [columna], end = ' ')
    print ()

print("Promedio por estudiantes: ")
estudiante1 = (int(listado[0][1])+int(listado[1][1])+int(listado[2][1])) / 3
estudiante2 = (int(listado[0][2])+int(listado[1][2])+int(listado[2][2])) / 3
estudiante3 = (int(listado[0][3])+int(listado[1][3])+int(listado[2][3])) / 3
estudiante4 = (int(listado[0][4])+int(listado[1][4])+int(listado[2][4])) / 3
estudiante5 = (int(listado[0][5])+int(listado[1][5])+int(listado[2][5])) / 3


print(f"El promedio del 1° estudiante es de: {estudiante1}")
print(f"El promedio del 2° estudiante es de: {estudiante2}")
print(f"El promedio del 3° estudiante es de: {estudiante3}")
print(f"El promedio del 4° estudiante es de: {estudiante4}")
print(f"El promedio del 5° estudiante es de: {estudiante5}")

print("Promedio por materia: ")

for i in range (len(listado)):
    promedio_materia = sum(listado[i][1:6])/5
    print(f"El promedio de la materia {listado[i][0]} es: {promedio_materia}")
#EJERCICIO 9

#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada

ta_te_ti = [["-","-","-"],["-","-","-"],["-","-","-"]]
jugada = int(input("Ingrese 1 para jugar: "))
#BIENVENIDOS AL TA-TE-TI!!

while jugada == 1:
        fila_tateti = int(input("Fila donde desea realizar su jugada"))
        columna_tateti = int(input("Columna donde desea realizar su jugada"))
        ta_te_ti[fila_tateti][columna_tateti] = input("Ingrese su jugada: X-O")

        for fila in range (len(ta_te_ti)):
            for columna in range(len(ta_te_ti[0])):
                print(ta_te_ti[fila][columna], end='  ')
            print()
        jugada = int(input("Ingrese 1 para jugar: "))
print("Gracias por jugar")