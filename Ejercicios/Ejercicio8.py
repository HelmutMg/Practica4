import sqlite3
import requests

def crear_conexion(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def crear_tabla_bitcoin(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bitcoin (
                fecha TEXT PRIMARY KEY,
                precio_usd DECIMAL,
                precio_gbp DECIMAL,
                precio_eur DECIMAL,
                precio_pen DECIMAL
            )
        """)
        conn.commit()
    except Error as e:
        print(e)


def insertar_datos_bitcoin(conn, fecha, precio_usd, precio_gbp, precio_eur, precio_pen):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)",
                       (fecha, precio_usd, precio_gbp, precio_eur, precio_pen))
        conn.commit()
    except Error as e:
        print(e)

def consultar_precio_compra(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        precio_pen = row[0]
        precio_eur = row[1]
        monto_compra_pen = 10 * precio_pen
        monto_compra_eur = 10 * precio_eur
        return monto_compra_pen, monto_compra_eur
    else:
        return None

def obtener_tipo_cambio_pen():
    url = "https://apis.net.pe/api/tipo-cambio/pen"
    try:
        response = requests.get(url)
        data = response.json()
        tipo_cambio_pen = data[0]["venta"]
        return tipo_cambio_pen
    except requests.exceptions.RequestException as e:
        print("Error al obtener el tipo de cambio de PEN:", e)
        return None

# Conectar a la base de datos
conn = crear_conexion("base.db")
if conn is not None:
    # Crear la tabla bitcoin si no existe
    crear_tabla_bitcoin(conn)

    # Obtener el tipo de cambio de PEN
    tipo_cambio_pen = obtener_tipo_cambio_pen()

   
    fecha = "2023-10-15"  
    precio_usd = 60000.00
    precio_gbp = 45000.00
    precio_eur = 52000.00

    precio_pen = precio_usd * tipo_cambio_pen

    insertar_datos_bitcoin(conn, fecha, precio_usd, precio_gbp, precio_eur, precio_pen)

   
    resultado = consultar_precio_compra(conn)
    if resultado is not None:
        monto_compra_pen, monto_compra_eur = resultado
        print(f"Precio de comprar 10 bitcoins en PEN: {monto_compra_pen} PEN")
        print(f"Precio de comprar 10 bitcoins en EUR: {monto_compra_eur} EUR")
    else:
        print("No hay datos disponibles para calcular el precio de compra.")

    conn.close()
else:
    print("No se pudo conectar a la base de datos.")
