import pandas as pd
def genSankey(df,cat_cols=[],value_cols=''):
    # maximum of 6 value cols -> 6 colors
    labelList = []
    for catCol in cat_cols:
        labelListTemp =  list(set(df[catCol].values))
        labelList = labelList + labelListTemp
        
    # remove duplicates from labelList
    labelList = list(dict.fromkeys(labelList))
    
    # define colors based on number of levels
    for i in range(len(cat_cols)-1):
        if i==0:
            sourceTargetDf = df[[cat_cols[i],cat_cols[i+1],value_cols]]
            sourceTargetDf.columns = ['source','target','count']
        else:
            tempDf = df[[cat_cols[i],cat_cols[i+1],value_cols]]
            tempDf.columns = ['source','target','count']
            sourceTargetDf = pd.concat([sourceTargetDf,tempDf])
        sourceTargetDf = sourceTargetDf.groupby(['source','target']).agg({'count':'sum'}).reset_index()
        sourceTargetDf['sourceID'] = sourceTargetDf['source'].apply(lambda x: labelList.index(x))
        sourceTargetDf['targetID'] = sourceTargetDf['target'].apply(lambda x: labelList.index(x))
        data = dict(
        type='sankey',
        node = dict(
          pad = 100,
          thickness = 100,
          line = dict(color = "black", width = 0.5),
          label = labelList,
        ),
          link = dict(
          source = sourceTargetDf['sourceID'],
          target = sourceTargetDf['targetID'],
          value = sourceTargetDf['count']
        )
      )
    layout =  dict(
        font = dict(
          size = 10,
        )
    )
       
    fig = dict(data=[data], layout=layout)
    return fig