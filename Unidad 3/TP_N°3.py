#TRABAJO PRACTICO NUMERO 3
#EJERCICIO1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input ("Ingrese su edad:"))
if edad >= 18:
    print ("Es mayor de edad")

#EJERCICIO2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
 
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("APROBADO")
else:
     print("DESAPROBADO")

#EJERCICIO3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero: "))
if numero % 2 == 0 :
    print("Ha ingresado un numero par.")
elif numero % 2 != 0:
    numero =  int(input("Por favor ingrese un numero par"))
    if numero % 2 == 0 :
        print("Ha ingresado un numero par")
    else:
        pass 

#EJERCICIO4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Por favor ingrese su edad: "))
#vamos a plantear las condiciones para clasificarlo en un grupo 

if edad > 0 and edad < 12:
    print ("Usted pertenece al grupo de niños.")
elif edad >= 12 and edad < 18 :
    print ("Usted pertenece al grupo de adolescentes.")
elif edad >= 18 and edad < 30 :
    print("Usted pertenece al grupo de Adulto Joven.")
elif edad >= 30:
    print("Usted pertences al grupo de Adultos.")
else:
    print("EDAD INVALIDA.")

#EJERCICIO5
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string

contra = input("Ingrese una contraseña" "\nLa contraseña debe tener 8 caracteres como minimo y 14 como maximo:  ")

long_contra = len (contra)


if long_contra >= 8 and long_contra <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#EJERCICIO6

#El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:

#importamos del paquete la moda, mediana, media
from statistics import mode, median, mean  
#importamos el paquete random
import random
#creamos una lista que tome 50 numeros aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range (50)]

moda = mode(numeros_aleatorios)
mediana = median (numeros_aleatorios)
media = mean (numeros_aleatorios)

print(numeros_aleatorios)

print (f"\nLa moda de los numeros ingresados es {moda}")
print (f"\nLa mediana de los numeros ingresados es {mediana}")
print (f"\nLa media de los numeros ingresados es {media}")
print("\nTeniendo en cuenta la lista de numeros ingresados: ")

#Hacemos una estructura para predecir la forma de una distribucion normal

if media > mediana and  mediana > moda :
    print ("\nLa lista tiene SESGO POSITIVO")
elif media < mediana and mediana < moda :
    print ("\nLa lista tiene SESGO NEGATIVO")
elif media == moda == mediana :
    print("\nLa lista NO TIENE SESGO")
else :
    print("La lista no tiene un sesgo definido")


