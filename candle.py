from candleUtil import candleUtil
import time

class Candle:

    def __init__(self, data, MA):
        self.timestamp = time.ctime(data[0]/1000)
        self.open = float(data[1])
        self.high = float(data[2])
        self.low = float(data[3])
        self.close = float(data[4])
        self.vol = float(data[5])
        self.closedUp = candleUtil.closedUp(self)
        self.closedDown = candleUtil.closedDown(self)
        self.shadow = self.high - self.low
        self.body = abs(self.open - self.close)
        self.MA = MA

    def toString(data):
        print(f'{data.timestamp}')
        print(f'\tOpen:\t{data.open}')
        print(f'\tClose:\t{data.close}')
        print(f'\tMA:\t{data.MA}')

        