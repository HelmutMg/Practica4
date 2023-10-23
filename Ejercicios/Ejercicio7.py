import requests
import sqlite3
from sqlite3 import Error

def crear_conexion(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def crear_tabla(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sunat_info (
                fecha TEXT PRIMARY KEY,
                compra DECIMAL,
                venta DECIMAL
            )
        """)
        conn.commit()
    except Error as e:
        print(e)

# Función para insertar datos en la tabla
def insertar_datos(conn, fecha, compra, venta):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))
        conn.commit()
    except Error as e:
        print(e)

# URL del API de SUNAT
url = "https://apis.net.pe/api/tipo-cambio/2023"

try:
    # Realizar la solicitud GET al API de SUNAT
    response = requests.get(url)
    data = response.json()

    # Conectar a la base de datos
    conn = crear_conexion("base.db")
    if conn is not None:
        # Crear la tabla si no existe
        crear_tabla(conn)
        
        # Insertar los datos del API en la tabla
        for item in data:
            fecha = item["fecha"]
            compra = item["compra"]
            venta = item["venta"]
            insertar_datos(conn, fecha, compra, venta)
        
        print("Datos almacenados en la base de datos.")
    else:
        print("No se pudo conectar a la base de datos.")

except requests.exceptions.RequestException as e:
    print("Error al realizar la solicitud al API de SUNAT:", e)

except Error as e:
    print("Error en la base de datos:", e)

finally:
    if conn:
        conn.close()

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    rows = cursor.fetchall()
    print("\nContenido de la tabla 'sunat_info':")
    for row in rows:
        print(row)

