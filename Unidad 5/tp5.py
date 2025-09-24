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