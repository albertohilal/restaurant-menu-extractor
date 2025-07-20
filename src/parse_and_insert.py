from utils import conectar, insertar_categoria, insertar_producto

CLIENTE_SLUG = "pertutti"
ARCHIVO_MENU = "output/menu_texto.txt"

def parsear_y_guardar():
    conn = conectar()
    cursor = conn.cursor()

    categoria_actual = None
    categoria_id = None
    descripcion_buffer = []
    nombre_producto = ""
    precio = 0

    with open(ARCHIVO_MENU, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            # Detectar nueva categoría si va en mayúsculas (ej: CAFÉ)
            if linea.isupper() and len(linea) > 2 and len(linea) < 40:
                if categoria_actual and nombre_producto:
                    descripcion = " ".join(descripcion_buffer).strip()
                    insertar_producto(cursor, categoria_id, CLIENTE_SLUG, nombre_producto, descripcion, precio)
                    descripcion_buffer = []
                    nombre_producto = ""
                    precio = 0

                categoria_actual = linea.title()
                categoria_id = insertar_categoria(cursor, categoria_actual)
                continue

            # Detectar producto + precio
            if "$" in linea:
                if categoria_actual and nombre_producto:
                    descripcion = " ".join(descripcion_buffer).strip()
                    insertar_producto(cursor, categoria_id, CLIENTE_SLUG, nombre_producto, descripcion, precio)

                partes = linea.rsplit("$", 1)
                nombre_producto = partes[0].strip(" .:-")
                try:
                    precio = int(partes[1].replace(".", "").replace("-", "").strip())
                except:
                    precio = 0
                descripcion_buffer = []
                continue

            # Agregar al buffer de descripción
            if linea:
                descripcion_buffer.append(linea)

        # Insertar el último producto si quedó pendiente
        if categoria_actual and nombre_producto:
            descripcion = " ".join(descripcion_buffer).strip()
            insertar_producto(cursor, categoria_id, CLIENTE_SLUG, nombre_producto, descripcion, precio)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    parsear_y_guardar()
