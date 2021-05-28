import json
import requests
import pprint as pp
from candle import Candle
from candleUtil import candleUtil
import argparse
import pandas as pan

OPEN = 'open'
HIGH = 'high'
LOW = 'low'
CLOSE = 'close'
INSIDE_BAR = 'insideBar'

INTERVAL = '1h'

data = []
CLOSES = []
klines = {}

def main():

    parser = argparse.ArgumentParser(description="Binance API Candles and stuff.")
    parser.add_argument("-$", "--symbol", type=str, metavar="symbol", default="BTCUSD", required=False, help="Crypto pair symbol. i.e. 'BTCUSD'")
    parser.add_argument("-p", "--pattern", type=str, metavar="pattern", default=None, required=False, help="Candlestick pattern to detect. i.e. 'Hammer'")
    parser.add_argument("-l", "--lookback", type=str, metavar="lookback", default="100", required=False, help="Number of Candles to pull.")
    parser.add_argument("-ma", "--movingavg", type=int, metavar="movingavg", default="20", required=False, help="Moving average rolling window size")
    args = parser.parse_args()

    WINDOW = args.movingavg

    url = f'https://api.binance.us/api/v3/klines?symbol={args.symbol}&interval={INTERVAL}&limit={args.lookback}'

    response = requests.get(f'{url}').json()

    ''' 
    load close of each candle into CLOSE_VALUES for indicator calculations 
    '''
    for i in range(len(response)):
        CLOSES.append(response[i][4]) 

    numbers_series = pan.Series(CLOSES)
    windows = numbers_series.rolling(WINDOW)
    moving_averages = windows.mean()

    moving_averages_list = moving_averages.tolist()
    MA = moving_averages_list[WINDOW - 1:]

    for i in range(len(response)):
        if i >= WINDOW-1:
            data.append(Candle(response[i], MA[i-WINDOW]))
        else:
            data.append(Candle(response[i], 0))

    if args.pattern == "hammer":
        for i in range(len(data)):
            if candleUtil.hammer(data[i]):
                print(f"{args.symbol} Hammer: \t" + data[i].timestamp)
                # print(f"SMA:\t\t{data[i].MA}")
                print()
    elif args.pattern == "insidebar":   
        for i in range(len(data)):
            if i > 0:
                if candleUtil.isInsideBar(data[i-1], data[i]):
                    print(f"{args.symbol} InsideBar: \t" + data[i].timestamp)
                    print()
                    # print(f"SMA:\t\t\t{data[i].MA}")
    elif args.pattern == "engulfing":   
        for i in range(len(data)):
            if candleUtil.bullBearEngulfing(data[i-1], data[i]):
                print(f"{args.symbol} Engulfing: \t" + data[i].timestamp)
                # print(f"SMA:\t\t\t{data[i].MA}")
                print()
    elif args.pattern == None:
        for i in range(len(data)):
            Candle.toString(data[i])

    

if __name__ == '__main__':
    main()