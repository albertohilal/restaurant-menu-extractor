# 🥗 Importador de Menú Pertutti

Este proyecto permite extraer productos y categorías desde un archivo de texto plano generado a partir del PDF de la carta del bar **Pertutti**, y guardarlos automáticamente en una base de datos MySQL, dentro de las tablas:

- `aa_menu_pertutti`
- `aa_categorias_pertutti`

El sistema fue desarrollado en Python y está pensado para facilitar la carga masiva de menús desde documentos escaneados.

---

## 🚀 Requisitos

- Python 3.8 o superior
- Base de datos MySQL (con las tablas mencionadas)
- Archivo de texto `menu_texto.txt` generado previamente a partir del OCR de la carta

---

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone git@github.com:albertohilal/menu-pertutti-importador.git
cd menu-pertutti-importador
Crear y configurar el archivo .env:

env
Copiar
Editar
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_password
DB_NAME=iunaorg_bares
Instalar dependencias (opcional):

Si se utilizan bibliotecas externas:

bash
Copiar
Editar
pip install -r requirements.txt
📝 Estructura del Proyecto
parse_and_insert.py: Script principal que lee el texto, detecta categorías y productos e inserta en la base.

utils.py: Funciones auxiliares para conexión a base de datos e inserciones SQL.

output/menu_texto.txt: Archivo plano generado a partir del PDF OCR (no se incluye por defecto).

▶️ Uso
bash
Copiar
Editar
python3 parse_and_insert.py
Al finalizar, los productos estarán cargados correctamente en la base de datos y listos para ser usados por el frontend.

✏️ Notas
Se espera que las categorías estén en mayúsculas en el archivo menu_texto.txt.

Los productos deben tener el formato:
Nombre del producto $Precio

Las descripciones (si las hay) van debajo, antes de la siguiente categoría o producto.

📂 Licencia
Este proyecto está bajo licencia MIT. Podés usarlo libremente para importar menús u otros documentos similares.

