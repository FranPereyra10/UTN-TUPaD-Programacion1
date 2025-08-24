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

#EJERCICIO7

#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

vocales = ["a","e","i","o","u"]

frase = input("Ingrese una frase: ")

ultimaletra = frase.lower()[len(frase)-1]

if ultimaletra in vocales:
    print (f"{frase}!")
else:
    print(frase)

#EJERCICIO8

#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

opcion = int(input("Ingrese una opcion\n1: Se imprimira su nombre en mayusculas. \n2: Se imprimira su nombre en minusculas. \n3: Se imprimira la pirmer letra de su nombre en Mayusculas\n:"))

nombre = input ("Ingrese su nombre: ")

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())


#EJERCICIO9

#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto registrado: "))

#Clsificamos el terremoto 

if magnitud < 3.00:
    print("El terremoto fue Muy Leve")
elif magnitud >= 3.00 and magnitud < 4.00:
    print("El terremoto fue Leve") 
elif magnitud >= 4.00 and magnitud < 5.00:
    print("El terremoto fue Moderado")
elif magnitud >= 5.00 and magnitud < 6.00:
    print ("El terremoto fue Fuerte")
elif magnitud >= 6.00  and magnitud < 7.00:
    print ("El terremoto fue Muy Fuerte")
elif magnitud > 7.00:
    print ("El terremoto fue Extremo")







