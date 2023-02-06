import json
from clickhouse_driver import Client
# import pandas as pd


def return_data(start_date, end_date):
    clickhouse_info = {
        "host": "192.168.8.96",
                "user": "da_team",
                "password": "Ftech@123"
    }
    client = Client(host=clickhouse_info['host'], user=clickhouse_info['user'],
                    password=clickhouse_info['password'], settings={
                        'use_numpy': True}
                    )
    query = f"""with data_2 as(select account_id,lpid,login_time,logout_time,online_time,date1_time,date2_time from da_cdp_funzy.partner_active_time
    group by account_id,lpid,login_time,logout_time,online_time,date1_time,date2_time),
    data_3 as(select *,toDate(case when date2_time=0 then login_time else logout_time END) as active_time from data_2),
    data_1 as(select account_id,create_time,lpid,uid,name,package,vnd,value,origin_total,total from da_cdp_funzy.partner_paid_user
    group by account_id,create_time,lpid,uid,name,package,vnd,value,origin_total,total),
    data1 as(
    select account_id,active_time,date1_time,date2_time,(CAST(date_add(day,1,toDate('{end_date}')) as DATE)-active_time) as recency  from data_3
    where active_time between '{start_date}' and '{end_date}'),
    data_rfd as(
    select sum(case when date2_time=0 then date1_time else date2_time END) as duration,account_id,min(recency) as recency,count(distinct active_time) as frequency
    from data1 where date2_time<=600 and date1_time<=600
    group by account_id
    order by account_id
    ),
    moneytary_data as(
    select account_id,sum(package) as monetary,sum(vnd) as vnd from data_1
    where toDate(create_time) between '{start_date}' and '{end_date}'
    group by account_id
    order by account_id),
    data_full as(
    select account_id,recency,frequency,duration as duration1,monetary,vnd from data_rfd left join moneytary_data on data_rfd.account_id=moneytary_data.account_id
    order by account_id),
    data_final as(
    select account_id,recency,frequency,monetary,round((duration1/frequency),3) as duration,vnd from data_full)
    select * from data_final
    """
    n = client.query_dataframe(query)
    return n
    

