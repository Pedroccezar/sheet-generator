import pandas as pd
import numpy as np
from gspread_dataframe import set_with_dataframe
import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credencial.json",
    scopes=scope
)

client = gspread.authorize(creds)
sheet = client.open_by_key("15SpGslotuwfz7Fzc6eSFAw690tEsepahhj9vq-3yHw8").sheet1

url = 'https://docs.google.com/spreadsheets/d/17p7v_DldO4hYvko52K_RLS-a9RCNEKuxsMbic--qx2g/export?format=csv'
planilha = pd.read_csv(url)
plantaourl = 'https://docs.google.com/spreadsheets/d/15SpGslotuwfz7Fzc6eSFAw690tEsepahhj9vq-3yHw8/export?format=csv'
planilha_def = pd.read_csv(plantaourl)

dias_nomes = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
dias_slugs = ['segunda', 'terca', 'quarta', 'quinta', 'sexta'] 

ultima_escala = {}
for dia in dias_nomes:
    if dia in planilha_def.columns:
        pessoas = planilha_def[dia].dropna().tolist()
        for p in pessoas:
            if p: ultima_escala[p] = dias_nomes.index(dia)

novas_listas = {
    'segunda': ['Bruno'], 
    'terca': ['Luiz'], 
    'quarta': ['Miguel'], 
    'quinta': ['Anna Carolina'], 
    'sexta': ['Nathan']
}
plantao_geral = ['Bruno', 'Luiz', 'Miguel', 'Anna Carolina', 'Nathan'] #Se precisar fixar plantão...

for i in planilha.itertuples():
    membro = i.membros
    if membro in plantao_geral:
        continue 
    
    index_anterior = ultima_escala.get(membro, -1)
    alvo_index = (index_anterior + 1) % 5
    
    alocado = False
    for tentativa in range(5):
        atual_index = (alvo_index + tentativa) % 5
        coluna_disponibilidade = dias_slugs[atual_index]
        
        if getattr(i, coluna_disponibilidade, False):
            novas_listas[coluna_disponibilidade].append(membro)
            plantao_geral.append(membro)
            alocado = True
            break

df_final = pd.DataFrame({
    'Segunda': pd.Series(novas_listas['segunda']),
    'Terça':   pd.Series(novas_listas['terca']),
    'Quarta':  pd.Series(novas_listas['quarta']),
    'Quinta':  pd.Series(novas_listas['quinta']),
    'Sexta':   pd.Series(novas_listas['sexta'])
}).fillna('')

sheet.batch_clear(["A:Z"])
set_with_dataframe(sheet, df_final)
print("Planilha atualizada!")

