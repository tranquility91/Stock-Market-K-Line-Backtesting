from FinMind.data import DataLoader
import pandas as pd
FM=DataLoader()
def getDataFM(prod,st,en):
    tmpdata=FM.taiwan_stock_daily_adj(stock_id=prod,start_date=st,end_date=en)
    tmpdata=tmpdata.rename(columns={'max':'high','min':'low','Trading_Volume':'volume'})
    tmpdata['date']=pd.to_datetime(tmpdata['date'])
    tmpdata=tmpdata.set_index(tmpdata['date'])
    tmpdata=tmpdata[['open','high','low','close','volume']]

    return tmpdata


