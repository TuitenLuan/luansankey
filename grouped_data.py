def grouped(data):
  n=data.groupby('Class',as_index=True).agg({'vnd':['sum','mean','min','max','std'],'account_id':'count','duration':['sum','mean','min','max','std']}).reset_index()
  n.loc[:,7]=round(n['vnd']['std']/n['vnd']['mean'],2)
  n.loc[:,8]=round(n['duration']['std']/n['duration']['mean'],2)
  return n