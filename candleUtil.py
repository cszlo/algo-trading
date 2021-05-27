class candleUtil:

    # returns > 0 if closed up, < 0 if closed down, 0 if flat
    def upDown(candle):
        if candle.open > candle.close:
            return False
        elif  candle.open < candle.close:
            return True
        else:
            return True

    # Returns True if curr is an inside bar, False if it is not
    def isInsideBar(prev, curr):
        if curr.closedUp:
            if prev.closedUp:
                return True if (curr.open >= prev.open and curr.close <= prev.close) else False
            if prev.closedDown:
                return True if (curr.close <= prev.open and curr.open >= prev.close) else False
        elif curr.closedDown:
            if prev.closedUp:
                return True if (curr.open <= prev.close and curr.close >= prev.open) else False
            if prev.closedDown:
                return True if (curr.close >= prev.close and curr.open <= prev.open) else False
        else:
            False

    # Returns + for bullish engulfing, negative for bearish engulfing
    def bullBearEngulfing(data, index):
        if index < 1:
            return False

        thisOpen= data[index][1]
        thisClose = data[index][4]
        thisDown = True if float(thisOpen) - float(thisClose) > 0 else False
        thisUp = not thisDown
        prevOpen = data[index-1][1]
        prevClose = data[index-1][4]
        prevDown = True if float(prevOpen) - float(prevClose) > 0 else False
        prevUp = not prevDown

        if thisUp and prevDown:
            return True if float(thisOpen) > float(prevClose) and float(thisClose) < float(prevOpen) else False
        if thisDown and prevUp:
            return True if float(thisOpen) < float(prevClose) and float(thisClose) > float(prevOpen) else False

    def hammer(candle):
        if candle.closedUp:
            return True if ((candle.open - candle.low) >= candle.body * 2) and ((candle.open - candle.low) > (candle.high - candle.close)*2) else False
        elif candle.closedDown:
            return True if ((candle.close - candle.low) >= candle.body * 2) and ((candle.close - candle.low) > (candle.high - candle.open)*2) else False
        else:
            return False