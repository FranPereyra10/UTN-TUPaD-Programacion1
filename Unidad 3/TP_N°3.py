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

