import pandas as pd
import pdfplumber
import re
import os

def CCMA():
    '''
    Función que lee todos los PDF de la carpeta 'PDF' y extrae los datos de los mismos. Luego hace una Tabla dinámica de control de los mismos.
    
    '''


    Texto = []
    df = pd.DataFrame()
    Archivos = []

    # Listar todos los PDF en 'PDF' con su ruta completa
    for root, dirs, files in os.walk('PDF'):
        for filename in files:
            #print(os.path.join(root, filename))
            Archivos.append(os.path.join(root, filename))

    # Filtrar los Archivos que no sean PDF
    Archivos = [x for x in Archivos if x.endswith(".pdf")]

    # Filtrar los Archivos que pesen menos de 10KB
    Archivos = [x for x in Archivos if os.path.getsize(x) > 10000]


    # Leer todas las páginas el PDF 'CCMA.pdf' de la carpeta 'PDF' e imprimir el resultado
    with pdfplumber.open('PDF/CCMA.pdf') as pdf:
        pages = pdf.pages
        for page in pdf.pages:
            Texto.append(page.extract_text())
            #print(page.extract_text())


    # Imprimir todos los RegEx del grupo 1 y 4 de la siguiente expresión regular r'(\d+/\d+)\s(Saldo)\s(\d+/\d+/\d+)\s(\d+.\d+)'

    for i in Texto:
        print(re.findall(r'(\d+/\d+)\s(Saldo)\s(\d+/\d+/\d+)\s(\d+.\d+)', i))

    # Exportar los resultados a un archivo CSV
    df = pd.DataFrame(re.findall(r'(\d+/\d+)\s(Saldo)\s(\d+/\d+/\d+)\s(\d+.\d+)', str(Texto)))
    df.to_csv('PDF/CCMA.csv', index=False, header=False)

if __name__ == "__main__":
    #obtener path anterior al actual
    PDFUbicación = os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PDFUbicación += "/PDF"
    CCMA(PDFPath=PDFUbicación)