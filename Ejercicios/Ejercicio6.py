def contar_lineas_codigo(Archivo):
    try:
        with open(Archivo, 'r') as f:
            lineas = f.readlines()
        lineas_codigo = 0
        for linea in lineas:
            linea = linea.strip()  
            if linea and not linea.startswith('#'):  
                lineas_codigo += 1
        return lineas_codigo
    except FileNotFoundError:
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    
    if not ruta_archivo.endswith(".py"):
        print("El archivo no tiene extensión .py")
        return
    
    try:
        num_lineas_codigo = contar_lineas_codigo(ruta_archivo)
        if num_lineas_codigo is not None:
            print(f"Archivo: '{ruta_archivo}', número de líneas de código: {num_lineas_codigo}")
        else:
            print("No se pudo abrir el archivo.")
    except FileNotFoundError:
        print("Ruta de archivo no válida.")

if __name__ == "__main__":
    main()
