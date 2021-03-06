# 1. Cree un script que almacene un número entero en una variable, y luego
# muestre en pantalla su valor absoluto, con el mensaje “El valor absoluto de N
# es |N|”. Finalmente, verifique que su programa funciona correctamente,
# ejecutándolo con el valor 10 en la variable (la salida debería ser 10), y luego
# con el valor -10 (la salida debería ser 10 nuevamente).

num = -10
print(f'El valor absoluto de N es {abs(num)}')

# --------------------------------------------------------------------------------

# 2. Cree un script que almacene su nombre de pila en una variable, y luego
# muestre en pantalla la cantidad de letras de ese nombre, con el mensaje “El
# nombre [NOMBRE] tiene [N] letras.”.

nombre = 'Matias'
print(f'El nombre {nombre} tiene {len(nombre)} letras.')

# --------------------------------------------------------------------------------

# 3. Cree un script que almacene, en dos variables, una base y un exponente, y
# luego muestre en pantalla el resultado de elevar el número base a la
# potencia exponente.

base = 10
exponente = 5
resultado = base ** exponente
print(resultado)

# --------------------------------------------------------------------------------

# 4. Implemente un algoritmo en Python para calcular el perímetro de un
# rectángulo, conociendo su base y altura. Los datos se deben almacenar en
# variables, y el resultado se debe mostrar en pantalla.
# perímetro = 2 * (base + altura)

base = 10
altura = 20
perimetro = 2 * (base + altura)
print(perimetro)

# --------------------------------------------------------------------------------

# 5. Implemente un algoritmo en Python para calcular el área de un rectángulo,
# conociendo su base y altura. Los datos se deben almacenar en variables, y el
# resultado se debe mostrar en pantalla.

base = 10
altura = 20
area = (base * altura)
print(area)

# --------------------------------------------------------------------------------

# 6. Implemente un algoritmo que intercambie los valores entre dos variables a y
# b cualesquiera. Por ejemplo, si a = 10 y b = 5, luego de ejecutar el algoritmo, la
# variable a debería ser igual 5, y la variable b debería ser igual a 10.

a = 10
b = 5

c = a 
a = b 
b = c

print(a,b)

# --------------------------------------------------------------------------------

# 7. En Python es posible resolver el problema del intercambio de valores sin
# hacer uso de variables adicionales, mediante la sintaxis de asignación
# múltiple. Investigue de qué se trata dicha funcionalidad, y utilízela para
# resolver el ejercicio anterior sin utilizar variables auxiliares/adicionales.

a = 10
b = 5
b,a = a,b

print(a,b)

# --------------------------------------------------------------------------------

# 8. Escriba un algoritmo que, conociendo las notas de los dos parciales de un
# alumno de la asignatura Introducción a la Programación, muestre en
# pantalla su promedio.

nota1 = 8
nota2 = 7
nota3 = 9

promedio = ((nota1 + nota2 + nota3) / 3)

print(promedio)

# --------------------------------------------------------------------------------

# 9. Cree un script que, sabiendo cuántos pesos argentinos tiene una persona
# ahorrada en su cuenta (almacenando ese monto en una variable), muestre
# en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =
# $14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
# formato:

ahorro = 300
dolar = 80.5
reales = 14.1
euros = 69.5

print(f"Usted tiene ${ahorro} pesos argentinos, los cuales se convierten en:")
print(f"- U${ahorro / dolar} dólares.")
print(f"- R${ahorro / reales} reales.")
print(f"- €{ahorro / euros} euros.")
