from sankey import genSankey
from conect_db import return_data
from merge_data import merge
from sankey import genSankey
import plotly.graph_objects as go
from data_score import df_create
from condition import condition
def sankey_visual(start_time_data1,end_time_data1,start_time_data2,end_time_data2):
    data1=return_data(start_time_data1,end_time_data1)
    data2=return_data(start_time_data2,end_time_data2)
    data1_x=df_create(data1)
    data1_x['Class']=data1_x.apply(condition,axis=1)
    data2_x=df_create(data2)
    data2_x['Class']=data2_x.apply(condition,axis=1)
    merge_data=merge(data1_x,data2_x)
    Hibernatting_source = genSankey(merge_data[merge_data['Class_x']=='Hibernatting_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    At_Risk_source = genSankey(merge_data[merge_data['Class_x']=='At Risk_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    Cant_lose_them_source = genSankey(merge_data[merge_data['Class_x']=='Cant Lose Them_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    About_to_sleep_source = genSankey(merge_data[merge_data['Class_x']=='About to Sleep_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    Need_attention_source = genSankey(merge_data[merge_data['Class_x']=='Need Attention_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    Loyal_user_source = genSankey(merge_data[merge_data['Class_x']=='Loyal User_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    Promising_source = genSankey(merge_data[merge_data['Class_x']=='Promising_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    Flash_customer_source = genSankey(merge_data[merge_data['Class_x']=='Flash Customer_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    Potential_loyalist_source = genSankey(merge_data[merge_data['Class_x']=='Potentital Loyalist_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    Champions_source = genSankey(merge_data[merge_data['Class_x']=='Champions_source'],cat_cols=['Class_x','Class_y'],value_cols='account_id')
    all = genSankey(merge_data,cat_cols=['Class_x','Class_y'],value_cols='account_id')
    updatemenus = [{'buttons': [{'method': 'animate',
                             'label': 'All',
                             'args': [all]
                              },
                            {'method': 'animate',
                             'label': 'Hibernatting_source',
                             'args': [Hibernatting_source]
                             },
                            {'method': 'animate',
                             'label': 'At_Risk_source',
                             'args': [At_Risk_source]
                             },
                             {'method': 'animate',
                             'label': 'Cant_lose_them_source',
                             'args': [Cant_lose_them_source]
                             },
                            {'method': 'animate',
                             'label': 'About_to_sleep_source',
                             'args': [About_to_sleep_source]
                             },
                                 {'method': 'animate',
                             'label': 'Need_attention_source',
                             'args': [Need_attention_source]
                             },
                                 {'method': 'animate',
                             'label': 'Loyal_user_source',
                             'args': [Loyal_user_source]
                             },
                                 {'method': 'animate',
                             'label': 'Promising_source',
                             'args': [Promising_source]
                             },
                             {'method': 'animate',
                             'label': 'Flash_customer_source',
                             'args': [Flash_customer_source]
                             },
                             {'method': 'animate',
                             'label': 'Potential_loyalist_source',
                             'args': [Potential_loyalist_source]
                             },
                            {'method': 'animate',
                             'label': 'Champions_source',
                             'args': [Champions_source]
                             }
                            
                          
                            ] } ]
    sank = genSankey(merge_data,cat_cols=['Class_x','Class_y'],value_cols='account_id')
    fig = go.Figure(sank)
    fig.update_layout(title_text="RFMD Transition data1-data2",
                    height=1000,
                    width=1000,
                    font_size=10)
    fig.update_layout(updatemenus=updatemenus)
    return fig