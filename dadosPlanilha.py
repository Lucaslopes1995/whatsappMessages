import pandas as pd

def getContatos():
  return pd.read_excel("contatos.xlsx",sheet_name="Planilha2")

contatos = getContatos()

# print(contatos)

# for i, mensagem in enumerate(contatos['nome']):
#   nome = contatos.loc[i,"nome"]
#   telefone = contatos.loc[i,"telefone"]

#   print(nome,telefone)

