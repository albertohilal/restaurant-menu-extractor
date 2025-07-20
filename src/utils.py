import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Configuración de conexión desde variables de entorno
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Nombre fijo del cliente (puede parametrizarse si se usa otro menú)
CLIENTE_SLUG = "pertutti"

def conectar():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def insertar_categoria(cursor, nombre_categoria):
    # Verificamos si ya existe
    query = "SELECT id FROM aa_categorias_pertutti WHERE nombre_categoria = %s"
    cursor.execute(query, (nombre_categoria,))
    result = cursor.fetchone()  # ✅ Consumimos el resultado pendiente
    if result:
        return result[0]
    else:
        insert_query = "INSERT INTO aa_categorias_pertutti (nombre_categoria) VALUES (%s)"
        cursor.execute(insert_query, (nombre_categoria,))
        return cursor.lastrowid

def insertar_producto(cursor, categoria_id, cliente_slug, nombre_producto, descripcion, precio):
    query = """
        INSERT INTO aa_menu_pertutti 
        (cliente_slug, categoria, nombre_producto, descripcion, precio, visible) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        cliente_slug,
        categoria_id,
        nombre_producto,
        descripcion,
        precio,
        1  # visible por defecto
    ))
