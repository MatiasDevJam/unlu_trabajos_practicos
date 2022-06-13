# 1. Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
# usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras,
# el programa simplemente debe mostrarlas en pantalla. Al detectar la palabra
# para detenerse, debe mostrar el mensaje “--- TERMINADO ---”.


# palabra = ""
# while palabra != "parar":
#    palabra = input("Ingrese una palabra: ")
#    print(f"La palabra ingresada es {palabra}")
# print("--- TERMINADO ---")

# --------------------------------------------------------------------------------

# 2. Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
# hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
# cargar. Una vez ingresadas las notas, el programa debe informar la nota
# promedio (tenga cuidado de no incluir al -1 dentro del promedio).

# def calcularPromedio():
#    promedio = 0
#    notaParcial = 0
#    total = 0
#    totalParciales = 0
#    while notaParcial != -1:
#       notaParcial = int(input("Ingrese su calificación: "))
#       if notaParcial >= 0:
#          total += notaParcial
#          totalParciales += 1
#          promedio = total / totalParciales
#       else:
#          print(f"La calificación promedio es {promedio}")

# calcularPromedio()

# --------------------------------------------------------------------------------

# 3. Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
# programa debe ser capaz de solicitarle al usuario que reingrese el número
# cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
# vez que detecte un error de validación, informele al usuario cuál fue el error, con
# los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
# fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
# válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.


# numero = 0
# terminado = True
# while terminado:
#    numero = input("Ingrese un número: ")
#    if numero.isalpha():
#       print("El dato ingresado no es numérico.")
#    elif int(numero) < 0 or int(numero) > 100:
#       print("El número ingresado está fuera del rango permitido.")
#    else:
#       int(numero)
#       terminado = False
#       print(f"{numero} es válido. Gracias!")
   
# --------------------------------------------------------------------------------

# 4. Construya un menú que le muestre al usuario lo siguiente:
# ********* MI PROGRAMA *********
# 1. Saludar.
# 2. Informar temperatura.
# 3. Mostrar nombre de materia.
# 4. Salir.
# Seleccione una opción [1-4]:
#
# ● - Cuando el usuario ingrese la opción 1, se mostrará el mensaje:
# “Hola, bienvenido a mi programa interactivo!”.
# ● - Cuando el usuario ingrese la opción 2, se mostrará el mensaje
# “Hay una sensación térmica de 20 grados Celsius.”.
# ● - Cuando el usuario ingrese la opción 3, se mostrará el mensaje
# “Estás en la materia Introducción a la Programación!”.
# ● - Cuando el usuario ingrese la opción 4, el programa debe terminar,
# mostrando el mensaje “Hasta la próxima!”.
# ● - Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
# inválida.”.
# Tip 1: crear al menos una función propia, que se encargue exclusivamente
# de mostrar el menú de opciones en pantalla.
# Tip 2: puede utilizar la instrucción os.system('cls') para limpiar la
# pantalla antes de volver a mostrar el menú. De esta manera su programa
# será más legible en la terminal. Para poder utilizar dicha instrucción
# deberá importar, al principio del script, la librería os de la siguiente
# manera:
#                             import os
#                             # su código
# Tip 3: antes de limpiar la pantalla y volver a mostrar el menú, puede
# esperar a que el usuario confirme que ha terminado de leer la información
# presentada, simplemente utilizando la función
# input(‘PRESIONE ENTER PARA CONTINUAR’).

# --------------------------------------------------------------------------------

# 5. Si bien el while es útil cuando desconocemos la cantidad de veces que
# repetiremos un bloque de instrucciones, también puede ser utilizado en los
# mismos casos que es utilizado el for (aunque la inversa no es verdadera).
# Rehaga todos los ejercicios del Trabajo Práctico VII utilizando un while en
# lugar de un for.

# n = 1
# while n <= 100:
#    print(n)
#    n += 1

#-----------------------------------------------------------------------------

# num = 1
# while num <= 100:
#    num += 1
#    if num % 2 == 0:
#       print(num)

#-----------------------------------------------------------------------------

# num = 75
# total = 0
# while num <= 150: 
#    total += num
#    num += 1
#    print(total)

#-----------------------------------------------------------------------------

