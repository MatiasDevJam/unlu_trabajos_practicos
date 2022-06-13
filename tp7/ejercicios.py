# 1. Cree un script para mostrar los primeros 100 números enteros positivos,
# comenzando desde el 1.

# for n in range(1, 101):
#     print(n)

# --------------------------------------------------------------------------------

# 2. Modifique el script del ejercicio anterior para que se muestren sólo los números
# pares. Para saber si un número es par, utilice el operador de módulo (%).

# for n in range(1, 101):
#      if n % 2 == 0:
#         print(n)

# --------------------------------------------------------------------------------

# 3. Cree un script para calcular el resultado de sumar los números desde el 75 al
# 150.

# for n in range(75, 151):
#     print(n + n)

# --------------------------------------------------------------------------------

# 4. Cree un script que le solicite al usuario ingresar un número entero, y muestre
# en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
# este ejercicio, pero recuerde que la función range no incluye al valor máximo
# enviado como parámetro.
# factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n

# num = int(input("Ingrese un número: "))

# factorial = 1

# for n in range(1, num+1):
#     factorial *= n
#     print(factorial)

# --------------------------------------------------------------------------------

# 5. Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
# uno, informarle si el mismo es positivo, negativo, o cero.


# for n in range(0, 10):
#     numeros = int(input("Ingrese un número: "))
#     if numeros > 0:
#         print("Numero positivo")
#     elif numeros == 0:
#         print("Igual a 0")
#     else:
#         print("Numero negativo")

# --------------------------------------------------------------------------------

# 6. Cree un script que le solicite al usuario ingresar 10 números, y una vez
# ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
# ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
# y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
# ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.

# numMax = 0
# posicion = 1

# for n in range(1, 11):
#     num = int(input("Ingrese un número: "))
#     if num > numMax:
#         numMax = num
#         posicion = n
# print(f"El numero mayor es {numMax} y la posicion es {posicion}")
    
# --------------------------------------------------------------------------------

# 7. Extienda el script del ejercicio anterior para que también informe el número
# mínimo ingresado, y su posición.

# numMax = 0
# numMin = 1000
# posicionMax = 1
# posicionMin = 1

# for n in range(1, 11):
#     num = int(input("Ingrese un número: "))
#     if num > numMax:
#         numMax = num
#         posicionMax = n
#     elif num < numMin:
#         numMin = num
#         posicionMin = n
# print(f"El numero menor es {numMin} y la posicion es {posicionMin}")
# print(f"El numero mayor es {numMax} y la posicion es {posicionMax}")

# --------------------------------------------------------------------------------

# 8. Un cliente ha solicitado un programa que le permita ingresar los mililitros de
# lluvia caídos diariamente en una semana, para que el programa le informe en
# pantalla el promedio de precipitación de esa semana. El cliente también desea
# saber cuál fue el día en que más llovió en la semana.
# A modo ilustrativo, un reporte generado por el programa debería verse como
# sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
#       El promedio de precipitaciones fue de XX mls. diarios.
#       El día de más precipitaciones fue el xxxxxx (nombre del día).
# Tenga en cuenta que la numeración de los días de la semana comienza con el 1
# para el día domingo.
# Codifique el programa para dar solución a lo solicitado por el cliente.

dias = 7
totalmilimetros = 0
promedio = 0
maxPrecipitacion = 0
diaSemana = ""

for n in range(1, dias+1):
    milimetros = int(input("Ingrese los mililitros del día: "))
    totalmilimetros += milimetros
    promedio = totalmilimetros // dias
    if milimetros > maxPrecipitacion:
        maxPrecipitacion = milimetros
        if n == 1:
            diaSemana = "Domingo"
        elif n == 2:
            diaSemana = "Lunes"
        elif n == 3:
            diaSemana = "Martes"
        elif n == 4:
            diaSemana = "Miercoles"
        elif n == 5:
            diaSemana = "Jueves"
        elif n == 6:
            diaSemana = "Viernes"
        elif n == 7:
            diaSemana = "Sabado"

print(f"El promedio de precipitaciones fue de {promedio} mls. diarios.")
print(f"El día de más precipitaciones fue el {diaSemana}")



