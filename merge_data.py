def merge(data1,data2):
  df_full=data1.merge(data2,on='account_id',how='left')
  new=df_full.dropna()
  n=new.groupby(['Class_x','Class_y'])['account_id'].agg('count').reset_index()
  n['Class_x'] =n['Class_x'].apply(lambda x: str(x)+'_source')
  n['Class_y'] =n['Class_y'].apply(lambda x: str(x)+'_target')
  return n