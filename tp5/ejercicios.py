# 1. Cree una función que reciba dos números como parámetro, y muestre en
# pantalla la suma aritmética de ambos. Invoque a la función con dos números
# leídos desde teclado

# def suma():
#     a = int(input("Ingrese un número: "))
#     b = int(input("Ingrese otro número: "))
#     resultado = a + b
#     print(f"La suma de ambos números es: {resultado}")

# suma()

# --------------------------------------------------------------------------------

# 2. Modifique el script del ejercicio anterior para que la función retorne el resultado
# en vez de mostrarlo. El programa debe seguir mostrando el resultado en
# pantalla.

# def suma():
#     a = int(input("Ingrese un número: "))
#     b = int(input("Ingrese otro número: "))
#     resultado = a + b
#     print(f"La suma de ambos números es: {resultado}")
#     return resultado

# suma()

# --------------------------------------------------------------------------------

# 3. Cree una función que reciba un string como parámetro, y retorne la cantidad de
# letras que posee. Luego, utilice la función para escribir un programa que solicite
# ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene
# ese nombre.

# def letrasCantidad(letras):
#     return len(letras)

# def nombreUsuario():
#     nombre = str(input("Ingrese su nombre: "))
#     print(f"Su nombre tiene {letrasCantidad(nombre)} letras")

# nombreUsuario()

# --------------------------------------------------------------------------------

# 4. Cree una función que reciba dos números como parámetro (base y exponente),
# y retorne el resultado de elevar base a la potencia exponente.

# def potencia(a, b):
#     resultado = a ** b
#     return resultado

# print(potencia(2, 3))

# --------------------------------------------------------------------------------

# 5. Cree una función que reciba un string como parámetro, y retorne el mismo
# string, pero con todas las letras convertidas a mayúsculas.

# def palabrasMayusculas(palabras):
#     palabras = palabras.upper()
#     print(palabras)
#     return palabras

# palabrasMayusculas("eres el mejor")

# --------------------------------------------------------------------------------

# 6. Modifique la función del ejercicio anterior para que retorne dos versiones del
# string recibido como parámetro: primero la versión en minúsculas, y luego la
# versión en mayúsculas.

# def conversor(palabras):
#     palabras = palabras.lower()
#     print(palabras)
#     palabras = palabras.upper()
#     print(palabras)
#     return palabras

# conversor("Game over")

# --------------------------------------------------------------------------------

# 7. Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
# y retorne True si nombre1 tiene más letras que nombre2, o False en caso
# contrario.

# def condicion(nombre1, nombre2):
#     nombre1 = len(nombre1)
#     nombre2 = len(nombre2)
#     if nombre1 > nombre2:
#         return False
#     else:
#         return True

# print(condicion("Perdiste", "Ganaste"))

# --------------------------------------------------------------------------------

# 8. Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
# llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
# un string cualquiera, y luego lo retorne. Luego cree otro archivo llamado
# programa_principal.py, que ejecute el programa haciendo uso de la función
# creada en el otro archivo.

