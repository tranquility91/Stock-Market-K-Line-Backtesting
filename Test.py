import pandas as pd
from main import getDataFM
from Chart import ChartCandle

prod = '00878'
data = getDataFM(prod, '2007-01-01', '2022-05-01')

#初始部位
position = 0
trade = pd.DataFrame()

#回測
for i in range(data.shape[0] - 1):
    #定義會用到的變數
    c_time = data.index[i]
    c_low = data.loc[c_time, 'low']
    c_high = data.loc[c_time, 'high']
    c_close = data.loc[c_time, 'close']
    c_open = data.loc[c_time, 'open']
    #取得下一期資料
    n_time = data.index[i + 1]
    n_open = data.loc[n_time, 'open']

    #進場程序
    if position == 0:
        #進場邏輯
        if c_close > c_open and (c_close - c_open) * 2 < (c_open - c_low):
            position = 1
            order_i = i
            order_time = n_time
            order_price = n_open
            order_unit = 1
    #出場程序
    elif position == 1:
        #出場邏輯
        if i > order_i + 3 and c_close > c_open:
            position = 0
            cover_time = n_time
            cover_price = n_open
            #交易紀錄
            trade = pd.concat([trade, pd.DataFrame([
                [prod, 'Buy', order_time, order_price, cover_time, cover_price, order_unit]
            ])], ignore_index=True)

print(trade)