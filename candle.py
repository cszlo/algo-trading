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
        self.closedUp = candleUtil.upDown(self)
        self.closedDown = not self.closedUp
        self.shadow = self.high - self.low
        self.body = abs(self.open - self.close)
        self.MA = MA

    def toString(data):
        print(f'{data.timestamp}')
        print(f'\tClose:\t{data.close}')
        print(f'\tMA:\t{data.MA}')
        print()

        