import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/17p7v_DldO4hYvko52K_RLS-a9RCNEKuxsMbic--qx2g/export?format=csv'
planilha = pd.read_csv(url)

seg = []



for i in planilha.itertuples():
    if i.segunda == True:
        seg.append(i.membros)
        print(i)