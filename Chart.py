import mplfinance

from main import getDataFM
import pandas as pd
import mplfinance as mpf
data = getDataFM('0050', '2020-01-01', '2022-01-02')

def ChartCandle(data) :
    mcolor=mpf.make_marketcolors(up='r',down='g',inherit=True)
    mstyle=mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mcolor)
    mpf.plot(data,type='candle',style= mstyle,volume=True)