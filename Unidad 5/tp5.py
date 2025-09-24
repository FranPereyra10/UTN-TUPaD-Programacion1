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
