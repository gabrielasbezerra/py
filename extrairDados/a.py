import tabula
import pandas as pd

# Ler o PDF
tabela_pdf = tabula.read_pdf(
    'planilhateste.pdf', pages='all', silent=True)[0]

# Alterar nomes de colunas; inplace = True atribui o novo nome da coluna direto
#tabela_pdf.rename(columns={'Nome': 'Name', 'Idade': 'Age'}, inplace=True)

# Excluir coluna/ axis = 1 é colunas axis = 0 é linha
#tabela_pdf.drop('Cidade', axis=1, inplace=True)

for tabela in tabela_pdf:
    print(tabela)

print(len(tabela_pdf))

# Converter o pdf para excel; especificar o nome da planilha; remover o índice automático;
tabela_pdf.to_excel('output.xlsx',
                    sheet_name='Planilha 1', index=False)
