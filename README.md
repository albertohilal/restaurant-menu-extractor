# 🧾 Restaurant Menu Extractor

Este proyecto permite extraer automáticamente **categorías y productos** desde menús escaneados o procesados con OCR y guardarlos en una base de datos **MySQL**, listos para usar en sistemas de gestión o sitios web.

---

## 🚀 Funcionalidad

- 📄 Procesa archivos de texto (`.txt`) generados por OCR a partir de menús en PDF o imagen.
- 🧠 Detecta y clasifica categorías de productos (como "Pizzas", "Bebidas").
- 🍕 Extrae el nombre del producto, su descripción y el precio.
- 🗃️ Inserta los datos en tablas `aa_categorias_*` y `aa_menu_*` de MySQL.

---

## 📂 Estructura

restaurant-menu-extractor/
│
├── output/ # Archivos de salida, opcional
├── src/ # Código fuente Python
│ ├── extract.py # Procesamiento del archivo de texto
│ ├── utils.py # Funciones de conexión e inserción
│ └── parse_and_insert.py # Script principal
├── .env # Configuración secreta (no se sube a git)
├── requirements.txt # Dependencias del proyecto
├── README.md # Este archivo
└── .gitignore



---

## ⚙️ Requisitos

- Python 3.10+
- MySQL server o conexión remota
- Dependencias Python:
  

pip install -r requirements.txt
🔐 Configuración
Crea un archivo .env con la conexión a tu base de datos:


MYSQL_HOST=localhost
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_clave
MYSQL_DATABASE=nombre_base
🧪 Ejecución
Asegurate de que menu_texto.txt (archivo OCR) esté en la raíz del proyecto.

Ejecutá el script:


python3 src/parse_and_insert.py
📝 Licencia
MIT © albertohilal