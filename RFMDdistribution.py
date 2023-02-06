from conect_db import return_data
from data_score import df_create
import pandas as pd
from condition import condition
from grouped_data import grouped
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def distribution(start_date,end_date):
    data1=return_data(start_date,end_date)
    data2=df_create(data1)
    data2['Class']=data2.apply(condition,axis=1)
    grouped_data=grouped(data2)
    specs = [[{'type':'pie'}]]
    fig1 = make_subplots(rows=1, cols=1, specs=specs, shared_yaxes = False)
    fig1.add_trace(go.Pie(labels=grouped_data['Class'],values=grouped_data['account_id']['count'],hole=0.6,
                                                        customdata=grouped_data[['vnd','duration',7,8]],
    hovertemplate="%{label}: <br>Account Number:%{value} </br>total_money:%{customdata[0][0]}</br>avg money:%{customdata[0][1]}</br>max money:%{customdata[0][3]}</br>min money:%{customdata[0][2]}</br>std money:%{customdata[0][4]}</br>cv money:%{customdata[0][10]}</br>min duration:%{customdata[0][7]}</br>max duration:%{customdata[0][8]}</br>std duration:%{customdata[0][9]}</br>average duration:%{customdata[0][6]}</br>cv duration:%{customdata[0][11]}"),1,1)

    fig1.update_layout(title_text="RFMD Class Distribution",
                    height=1000,
                    width=700,
                    font_size=15)
    return fig1
    

    

