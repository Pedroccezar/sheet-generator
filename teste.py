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

seg, ter, qua, qui, sex, plantao = [], [], [], [], [], []

for i in planilha.itertuples():
    if i.segunda:
        seg.append(i.membros)
        plantao.append(i.membros)
        
    elif i.terca and not i.membros in plantao:
        ter.append(i.membros)
        plantao.append(i.membros)
    

    elif i.quarta and not i.membros in plantao:
        qua.append(i.membros)
        plantao.append(i.membros)
        
    elif i.quinta and not i.membros in plantao:
        qui.append(i.membros)
        plantao.append(i.membros)
        
    elif i.sexta and not i.membros in plantao:
        sex.append(i.membros)
        plantao.append(i.membros)
        
print(f'segunda:{seg}, terca: {ter}, quarta: {qua}, quinta: {qui}, sexta: {sex}')

planilha_def = pd.DataFrame({
    'Segunda': pd.Series(seg),
    'Terça': pd.Series(ter),
    'Quarta': pd.Series(qua),
    'Quinta': pd.Series(qui),
    'Sexta': pd.Series(sex)
})

planilha_def = planilha_def.fillna('')
set_with_dataframe(sheet, planilha_def)
planilha_def.head(10)