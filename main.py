from typing import Union
from fastapi import FastAPI
from conect_db import return_data
from visual import visual_dash
from visual_sankey import sankey_visual
from sankey_push import visual_sankey_push

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getvisual_distribution_RFMD")
def get_visual(start_date: str, end_date: str):
    return visual_dash(start_date, end_date)
@app.get("/visual_RFMD_transition")
def get_visual_transition(start_date_data1:str,end_date_data1:str,start_date_data2:str,end_date_data2:str):
    return visual_sankey_push(start_date_data1, end_date_data1,start_date_data2,end_date_data2)

