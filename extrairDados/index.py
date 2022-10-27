import PyPDF2
import re
import pandas as pd
import tabula

# Abrindo o arquivo em modo leitura e lendo o binario/rb; salvou o objeto de arquivo como pdfFileObj
pdfFileObj = open('planilhateste.pdf', 'rb')

# Passa o objeto de arquivo pdf e obtem um objeto leitor de pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

# Imprime o número de páginas
print('Número de páginas é igual a ' + str(pdfReader.numPages))

#  Recebe o número da página (começando com o índice 0) como argumento e retorna o objeto da página
pageObj = pdfReader.getPage(0)

# O objeto de página tem a função extractText() para extrair texto da página PDF
print(pageObj.extract_text())

df = ('planilhateste.pdf')
output = 'output.csv'
tabula.convert_into(df, output, output_format="csv",
                    stream=True, pages='all')[0]

pdfFileObj.close()
