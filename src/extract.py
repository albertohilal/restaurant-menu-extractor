import pdfplumber
from dotenv import load_dotenv
import os

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")

def extract_text():
    if not os.path.exists(PDF_PATH):
        print(f"❌ No se encontró el archivo: {PDF_PATH}")
        return

    with pdfplumber.open(PDF_PATH) as pdf:
        all_text = ""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                all_text += f"\n\n### Página {i + 1} ###\n{text}"

    return all_text

if __name__ == "__main__":
    contenido = extract_text()
    if contenido:
        with open("output/menu_texto.txt", "w", encoding="utf-8") as f:
            f.write(contenido)
        print("✅ Texto extraído en: output/menu_texto.txt")
