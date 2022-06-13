import os

def menu():
    print("1. Saludar.")
    print("2. Informar temperatura.")
    print("3. Mostrar nombre de materia.")  
    print("4. Salir. \n")
   

terminado = True
opcion = 0
while terminado:
    menu()
    opcion = int(input("Seleccione una opción [1-4]: "))
    if opcion == 1:
        os.system('cls')
        print("Hola, bienvenido a mi programa interactivo! \n")
    elif opcion == 2:
        os.system('cls')
        print("Hay una sensación térmica de 20 grados Celsius. \n")
    elif opcion == 3:
        os.system('cls')
        print("Estás en la materia Introducción a la Programación! \n")
    elif opcion == 4:
        print("Hasta la próxima! \n")
        terminado = False
    else:
        print("Opción inválida. \n")
        
    input("Presione enter para continuar...")

