# 1. Cree un script que le solicite al usuario ingresar un número por teclado, y
# luego le informe en pantalla si su número es mayor que 10; antes de finalizar
# e independientemente de lo que haya sucedido antes, el script mostrará un
# mensaje de despedida. Ejemplos de cómo debería verse la salida del script:

# num = int(input("Ingrese un número: "))

# if num > 10:
#     print(f"{num} es mayor que 10!")

# print("Saludos")

# --------------------------------------------------------------------------------

# 2. Modifique el script anterior para que mantenga el funcionamiento, pero
# ahora, cuando el número no es mayor que 10, también se muestre un
# mensaje “Tu número (N) es menor o igual que 10!”

# num = int(input("Ingrese un número: "))

# if num > 10:
#     print(f"Tú {num} es mayor que 10!")
# else:
#     print(f"Tú {num} es menor o igual que 10!")

# print("Saludos")

# --------------------------------------------------------------------------------

# 3. Cree un script que le solicite al usuario ingresar dos números por teclado, y
# luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
# de que los números sean iguales, y muestre un mensaje acorde.

# num1 = int(input("Ingrese un número: "))
# num2 = int(input("Ingrese otro número: "))

# if num1 > num2:
#     print(f"{num1} es mayor")
# elif num2 > num1:
#     print(f"{num2} es mayor")
# else:
#     print(f"{num1} y {num2} son iguales")

# --------------------------------------------------------------------------------

# 4. Cree un script que le solicite al usuario ingresar un número por teclado, y le
# informe con un mensaje si su número es positivo, negativo, o 0.

# num = int(input("Ingrese un número: "))

# if num > 0:
#     print(f"{num} es positivo")
# elif num < 0:
#     print(f"{num} es negativo")
# else:
#     print(f"{num} es 0")

# --------------------------------------------------------------------------------

# 5. Cree un script que, dado un número de día de la semana ingresado por
# teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
# números y días de la semana es la siguiente:

# diaSemana = int(input("Ingrese día de la semana: "))

# if diaSemana == 1:
#     print("Domingo")
# elif diaSemana == 2:
#     print("Lunes")
# elif diaSemana == 3:
#     print("Martes")
# elif diaSemana == 4:
#     print("Miercoles")
# elif diaSemana == 5:
#     print("Jueves")
# elif diaSemana == 6:
#     print("Viernes")
# elif diaSemana == 7:
#     print("Sábado")
# else:
#     print("No es un día válido")

# --------------------------------------------------------------------------------

# 6. Cree un script que le solicite a un alumno de la asignatura Introducción a la
# Programación que ingrese las notas de sus dos parciales. Como resultado, se
# le debe informar al alumno su situación, junto con la nota promedio. Las
# reglas para saber la situación de un alumno son las siguientes:

# nota1 = int(input("Ingrese la nota del primer parcial: "))
# nota2 = int(input("Ingrese la nota del segundo parcial: "))

# promedio = (nota1 + nota2) / 2

# if promedio >= 8 and nota1 >= 4 and nota2 >= 4:
#     print(f"Promovido, su nota es {promedio}")
# elif promedio >= 4 and nota1 >= 4 and nota2 >= 4:
#     print(f"Regular, su nota es {promedio}")
# else:
#     print(f"Libre, su nota es {promedio}")

# --------------------------------------------------------------------------------

# 7. Cree un script que determine si un triángulo es isósceles, equilátero, o
# escaleno. Para determinar esto, se le solicitará al usuario ingresar tres
# números, correspondientes a los tres lados del triángulo.

# lado1 = int(input("Ingrese el lado del triángulo: "))
# lado2 = int(input("Ingrese el lado del triángulo: "))
# lado3 = int(input("Ingrese el lado del triángulo: "))

# if lado1 == lado2 and lado1 == lado3:
#     print("Es equilátero")
# elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
#     print("Es escaleno")
# else:
#     print("Es isósceles")

# --------------------------------------------------------------------------------

# 8. Las estructuras alternativas pueden utilizarse para validar datos. Por
# ejemplo, si se intenta crear una función que tome dos enteros como
# parámetro y muestre el resultado de su división, puede ocurrir un error si el
# denominador es cero. Utilice la estructura alternativa para validar que el
# denominador no sea cero; en caso de serlo, la función deberá mostrar el
# mensaje “No se puede dividir por 0!” en lugar de intentar mostrar el
# resultado.


# def division(num1, num2):
#     if num2 != 0:
#         print(num1 // num2)
#     else:
#         print("No se puede dividir por 0!")
#         return num1, num2

# division(10, 0)

# --------------------------------------------------------------------------------

# 9. Python ofrece algunas funciones built-in para facilitar la implementación de
# validaciones. A continuación se listan algunas de las más comunes:
#
#     valor.isdigit()
#     Retorna True si todos los caracteres de valor son numéricos, False en caso
#     contrario.
#
#     valor.isalpha()
#     Retorna True si todos los caracteres de valor son alfabéticos (no
#     numéricos), False en caso contrario.
#
#     valor.isalnum()
#     Retorna True si valor es una combinación alfanumérica (caracteres y
#     números), False en caso contrario.
#
# Codifique una función que reciba un parámetro cualquiera proveniente del
# usuario del programa (que puede contener letras, números, o una combinación
# de ambas), e indique si el mismo es un número, una palabra, o un valor
# alfanumérico. Compruebe que su función resuelve el problema enviándole
# valores correspondientes a las tres posibilidades.

parametro = input("Ingrese parametro: ")

def validacion(parametro):
    
    if parametro.isdigit():
        print("Es númerico")
    elif parametro.isalpha():
        print("Es alfabético")
    elif parametro.isalnum():
        print("Es alfanumérico")
    else:
        print("No se reconoce el parámetro")

validacion(parametro)