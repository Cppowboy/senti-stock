import json
import os
from collections import Counter
# import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import datetime as DT
from datetime import datetime


def get_hist(sym, start="2015-01-01", end="2018-01-01"):
    data = pdr.get_data_yahoo(sym, start, end)
    return data['Close']


if __name__ == '__main__':
    yf.pdr_override()
    min_news_number = 500
    threshold = 0.01
    filename = 'long.json'
    day_number = 30
    fout = open(filename, 'w', encoding='utf-8')
    data_list = []
    for filename in os.listdir('.'):
        symbol, ext = os.path.splitext(filename)
        print('processing ', symbol)
        if ext == '.json' and symbol != 'middle' and symbol != 'short':
            try:
                data = json.load(open(filename, 'r', encoding='utf-8'))
            except Exception as e:
                print(e, 'error in decode json')
            print(len(data), 'pieces of news')
            if len(data) < min_news_number:
                continue
            try:
                close = get_hist(symbol)
            except Exception as e:
                print(e, 'error in gettting history data')
            print('get history close price', len(close))
            for item in data:
                try:
                    symbol, title, date_str = item['symbol'], item['title'], item['date']
                    dt = datetime.strptime(date_str, '%m%d%Y')
                    next_dt = dt + DT.timedelta(days=day_number)
                    this_date_str = datetime.strftime(dt, '%Y-%m-%d')
                    next_date_str = datetime.strftime(next_dt, '%Y-%m-%d')
                    this_close = close[this_date_str]
                    next_close = close[next_date_str]
                    rate = next_close / this_close - 1
                    if rate > threshold:
                        p = 1
                    elif rate < - threshold:
                        p = -1
                    else:
                        p = 0
                    data_list.append({
                        'symbol': symbol,
                        'title': title,
                        'date_str': date_str,
                        'this_close': this_close,
                        'next_close': next_close,
                        'rate': rate,
                        'polarity': p
                    })
                except Exception as e:
                    print(e)
    json.dump(data_list, fout)
