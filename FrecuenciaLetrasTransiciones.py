import PyPDF2
from collections import Counter
import string

def contar_letras_y_transiciones_pdf(ruta_pdf):
    # Abrir el archivo PDF
    with open(ruta_pdf, "rb") as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        texto = ""

        # Leer todas las páginas del PDF
        for pagina in lector_pdf.pages:
            texto += pagina.extract_text() or ""

    # Convertir el texto a minúsculas y filtrar solo letras (incluyendo 'ñ')
    texto = texto.lower()
    texto_filtrado = ''.join(filter(lambda c: c in string.ascii_lowercase or c == 'ñ', texto))

    # Contar las letras
    contador_letras = Counter(texto_filtrado)

    # Contar transiciones (pares de letras consecutivas)
    transiciones = Counter()
    for i in range(len(texto_filtrado) - 1):
        par = texto_filtrado[i:i + 2]
        transiciones[par] += 1

    # Resultados
    total_letras = sum(contador_letras.values())
    return total_letras, contador_letras, transiciones

# Especificar la ruta del archivo PDF
ruta_pdf = r"C:\Users\AsusTuf\Downloads\quijote2.pdf"

# Contar letras y transiciones en el PDF
total_letras, conteo_letras, conteo_transiciones = contar_letras_y_transiciones_pdf(ruta_pdf)

# Imprimir resultados
print(f"Total de letras: {total_letras}")
print("Frecuencia de cada letra (ordenado alfabéticamente):")

# Ordenar el conteo de letras alfabéticamente y mostrar
for letra in sorted(conteo_letras.keys()):
    print(f"{letra}: {conteo_letras[letra]}")

print("\nFrecuencia de pares de letras consecutivas:")
# Imprimir las transiciones en orden alfabético
for par in sorted(conteo_transiciones.keys()):
    print(f"{par}: {conteo_transiciones[par]}")
