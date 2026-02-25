import pandas as pd
import numpy as np

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
        
    elif i.terca and not i.membros in plantao:
        qui.append(i.membros)
        plantao.append(i.membros)
        
    elif i.terca and not i.membros in plantao:
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

planilha_def['Segunda'] = np.where(planilha_def['Segunda'].isna(),'',planilha_def['Segunda'])
planilha_def['Terça'] = np.where(planilha_def['Terça'].isna(),'',planilha_def['Terça'])
planilha_def['Quarta'] = np.where(planilha_def['Quarta'].isna(),'',planilha_def['Quarta'])
planilha_def['Quinta'] = np.where(planilha_def['Quinta'].isna(),'',planilha_def['Quinta'])
planilha_def['Sexta'] = np.where(planilha_def['Sexta'].isna(),'',planilha_def['Sexta'])

planilha_def.head(10)