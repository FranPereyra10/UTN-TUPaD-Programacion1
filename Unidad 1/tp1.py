#Este es todo el contenido del tp1
#EJERCICIO1
print("Hola Mundo!")
#EJERCICIO2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
#EJERCICIO3
nombre3 = input("Ingrese su nombre: ")
apellido3 = input("Ingrese su apellido: ")
residencia3 = input("Ingrese su pais de origen: ")
edad3 = int(input("Ingrese su edad: "))
print(f"Hola, soy {nombre3} {apellido3}, tengo {edad3} años y soy de {residencia3}")
#EJERCICIO4
radio = float(input("Ingrese el radio del circulo: "))
area = 3.14 * (radio**2)
perimetro = 2*3.14*radio
print( f"El area de la circunferencia es de: {area}, y su perimetro es: {perimetro}")
#EJERCICIO5
segundos = float(input("Ingrese los segundos: "))
horas = segundos/3600
print (f"Los segundos ingresados equivalen a {horas}, horas")
#EJERCICIO6
numero6 = int(input("Ingrese un numero"))
for i in range(1,11):
  print ( f"{numero6} x {i} = { numero6*i}" )
#EJERCICIO7
numero7_1 = int(input("Ingrese un numero distinto de cero: "))
numero7_2 = int(input("Ingrese otro numero distinto de cero:"))
if numero7_1 != 0 and numero7_2 != 0:
    suma = numero7_1 + numero7_2
    resta = numero7_1 - numero7_2
    multiplicacion = numero7_1*numero7_2
    division = numero7_1/numero7_2
    print(f"La suma es: {suma} \nLa resta es: {resta} \n La multiplicacion es: {multiplicacion} \nLa division es: {division}") 
else:
    print("ERROR: Uno de los numeros es cero")
#EJERCICIO8
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura**2)
print(f"Su IMC es de: {imc}")
#EJERCICIO9
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
Fahrenheit = (celsius * (9/5)) + 32
print(f"Su equivalente en Fahrenheit es: {Fahrenheit} ")
#EJERCICIO10
numero10_1 = float(input("Ingrese un numero:"))
numero10_2 = float(input("Ingrese un segundo numero:"))
numero10_3 = float(input("Ingrese un tercer numero: "))

promedio = (numero10_1+numero10_2+numero10_3) / 3
print(f"El promedio de los numeros ingresados es: {promedio}")


#ESTE COMENTARIO ES DE PRUEBA PARA PROBAR MI RAMA PERSONAL