import plotly.io as pio
import plotly.graph_objects as go
from visual_sankey import sankey_visual

def visual_sankey_push(start_date_data1,end_date_data1,start_date_data2,end_date_data2):

  # init tab (browser)
  pio.renderers.default = 'browser'



  ## get_data_luanly
  ## fuction getdata(start_date,end_date)
  # data = getdata(start_date,end_date)



  # process chart
  
  sankey_plot = sankey_visual(start_date_data1,end_date_data1,start_date_data2,end_date_data2)






  return pio.show(sankey_plot)

