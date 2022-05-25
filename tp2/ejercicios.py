# 1. Abra la consola de Python y escriba las instrucciones necesarias para mostrar el
# mensaje “HOLA MUNDO”, y luego el resultado de la operación 3 + 4.

print('HOLA MUNDO')
print( 3 + 4)

# --------------------------------------------------------------------------------

# 2. Utilizando el editor de código que prefiera, cree un script llamado
# hola_mundo.py que realice las mismas operaciones que en el ejercicio
# anterior. Guarde el script y ejecútelo (mediante una terminal, o la IDE que
# esté utilizando).

# --------------------------------------------------------------------------------

# 3. Cree un nuevo script llamado pruebas.py, y luego copie y pegue el siguiente
# contenido:

    # pint('Esto es una prueba')
    # print(10 - 1)

# Ejecute el script. ¿Qué ha sucedido? Lea detenidamente el error, e intente
# descubrir qué nos está diciendo el intérprete de Python. ¿En qué línea está el
# error? ¿Puede corregirlo?

# --------------------------------------------------------------------------------

# 4. Un colega programador nos ha proporcionado un script que resuelve la
# multiplicación de dos números y muestra el resultado en pantalla; el
# contenido del script es el siguiente:

numero1 = 10
numero2 = 5
resultado = numero1 * numero2
print('El producto entre ' + str(numero1) + ' y ' + str(numero2) + ' da ' + str(resultado))

# Ejecute el código para verificar el funcionamiento del script, y luego analice
# detenidamente el código y responda:
# - ¿Qué son numero1, numero2, y resultado?
# - ¿Por qué es necesario utilizar la función str(...) para mostrar en pantalla los
# valores de numero1, numero2, y resultado?

# --------------------------------------------------------------------------------

# 5. Cree un script llamado mi_nombre.py, el cual almacene su nombre completo
# en una variable, y luego lo muestre en pantalla.

# --------------------------------------------------------------------------------

# 6. Modifique el código del ejercicio anterior para que el nombre se almacene en
# una variable, y el apellido en otra. Además, introduzca una tercera variable
# para almacenar su edad. Ahora, en pantalla muestre el mensaje “Mi nombre
# completo es [NOMBRE] [APELLIDO] y tengo [EDAD] años.”.

# --------------------------------------------------------------------------------

# 7. Cree un script llamado numero_favorito.py, y almacene su número favorito en
# una variable. Luego muestre en pantalla el mensaje “Mi número favorito es [N]”.

# --------------------------------------------------------------------------------

# 8. Se le ha solicitado a dos programadores que resuelvan el mismo problema:
# conociendo el total de inscriptos de una asignatura y cuántos alumnos han
# asistido a la clase de hoy, queremos un programa que nos muestre en
# pantalla el porcentaje de asistencia del día de hoy. Las dos versiones que
# realizaron los programadores son:

# Programador A
# almaceno cuántos alumnos asistieron a la clase de hoy
alumnos_presentes = 35
# almaceno el total de inscriptos en la asignatura
alumnos_inscriptos = 54
# calculo del porcentaje de alumnos presentes en la clase de hoy
porcentaje_presentes = (alumnos_presentes * 100) / alumnos_inscriptos
# muestro el porcentaje calculado en pantalla
print('Hoy asistió el ' + str(porcentaje_presentes) + ' porciento del alumnado.')

# Programador B
p = 35
i = 54
pp = (p * 100) / i
print('Hoy asistió el ' + str(pp) + ' % del alumnado.')

# Analice detenidamente ambas versiones, y luego responda:
# - ¿Ambas versiones resuelven el problema?.
# Si.
# - ¿Cuál versión es más legible y fácil de comprender?.
# La versión del Programador A
# - ¿Qué desventajas tiene escribir código en la forma en que lo hace el
# Programador B?.
# Es ilegible y dificil de mantener.
