def guardar_tabla_de_multiplicar(numero):
    if 1 <= numero <= 10:
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
        print(f"La tabla de multiplicar para {numero} se ha guardado en tabla-{numero}.txt")
    else:
        print("El número debe estar entre 1 y 10.")

def mostrar_tabla_de_multiplicar(numero):
    if 1 <= numero <= 10:
        try:
            with open(f"tabla-{numero}.txt", "r") as archivo:
                contenido = archivo.read()
                print(f"Tabla de multiplicar para {numero}:\n{contenido}")
        except FileNotFoundError:
            print(f"El archivo tabla-{numero}.txt no existe.")
    else:
        print("El número debe estar entre 1 y 10.")

def mostrar_linea_de_tabla(numero, linea):
    if 1 <= numero <= 10:
        try:
            with open(f"tabla-{numero}.txt", "r") as archivo:
                lineas = archivo.readlines()
                if 1 <= linea <= 10:
                    if len(lineas) >= linea:
                        print(f"Línea {linea} de la tabla de multiplicar para {numero}: {lineas[linea - 1]}")
                    else:
                        print("La línea especificada no existe en el archivo.")
                else:
                    print("El número de línea debe estar entre 1 y 10.")
        except FileNotFoundError:
            print(f"El archivo tabla-{numero}.txt no existe.")

def main():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            numero = int(input("Introduzca un número entre 1 y 10: "))
            guardar_tabla_de_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Introduzca un número entre 1 y 10: "))
            mostrar_tabla_de_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Introduzca un número entre 1 y 10: "))
            linea = int(input("Introduzca un número de línea entre 1 y 10: "))
            mostrar_linea_de_tabla(numero, linea)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

