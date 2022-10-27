import PyPDF2


# Abrindo arquivos modo binario e leitura
arquivo1 = open('planilhateste.pdf', 'rb')
arquivo2 = open('planilhateste2.pdf', 'rb')

# Lendo os dados do binario, que são de PDF
dados_do_arq1 = PyPDF2.PdfFileReader(arquivo1)
dados_do_arq2 = PyPDF2.PdfFileReader(arquivo2)

# Declarando um objeto do tipo Merge
merge = PyPDF2.PdfFileMerger()
# Dando append no Merge dos meus dados de PDF
merge.append(dados_do_arq1)
merge.append(dados_do_arq2)

# Escrevendo o novo arquivo pdf
merge.write('arquivodesaidamerge.pdf')
