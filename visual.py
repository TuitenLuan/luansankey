import plotly_express as px
import plotly.io as pio
import plotly.graph_objects as go
from RFMDdistribution import distribution

def visual_dash(start_date,end_date):

  # init tab (browser)
  pio.renderers.default = 'browser'



  ## get_data_luanly
  ## fuction getdata(start_date,end_date)
  # data = getdata(start_date,end_date)



  # process chart
  
  scatter_plot = distribution(start_date,end_date)






  return pio.show(scatter_plot)
