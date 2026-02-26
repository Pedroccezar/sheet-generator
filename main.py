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

seg, ter, qua, qui, sex, plantao = ['Bruno'], ['Luiz'], ['Miguel'], ['Anna Carolina'], ['Nathan'], [] #Se precisar fixar plantão...

for i in planilha.itertuples():

    if i.membros not in plantao:

        menor = min(len(seg), len(ter), len(qua), len(qui), len(sex))

        if i.segunda and len(seg) == menor:
            seg.append(i.membros)
            plantao.append(i.membros)

        elif i.terca and len(ter) == menor:
            ter.append(i.membros)
            plantao.append(i.membros)

        elif i.quarta and len(qua) == menor:
            qua.append(i.membros)
            plantao.append(i.membros)

        elif i.quinta and len(qui) == menor:
            qui.append(i.membros)
            plantao.append(i.membros)

        elif i.sexta and len(sex) == menor:
            sex.append(i.membros)
            plantao.append(i.membros)


planilha_def = pd.DataFrame({
    'Segunda': pd.Series(seg),
    'Terça': pd.Series(ter),
    'Quarta': pd.Series(qua),
    'Quinta': pd.Series(qui),
    'Sexta': pd.Series(sex)
})

planilha_def = planilha_def.fillna('')
set_with_dataframe(sheet, planilha_def)
print("Planilha Feita!")

