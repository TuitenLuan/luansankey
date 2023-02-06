import pandas as pd
def df_create(data):
        data['R_rank']=pd.cut(data['recency'],5,labels=['5','4','3','2','1'])
        data['F_rank']=pd.cut(data['frequency'],5,labels=['1','2','3','4','5'])
        return data
