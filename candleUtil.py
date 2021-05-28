class candleUtil:

    # Returns 1 if closed up, -1 if closed down, 0 if flat
    def upDown(candle):
        if candle.open > candle.close:
            return 1
        elif  candle.open < candle.close:
            return -1
        else:
            return 0

    # Returns True if curr is an inside bar, False if it is not
    # 
    # Investopedia: Inside Day(bar)
    # An inside day is a two-day price pattern that occurs when a second day 
    # has a range that is completely inside the first day's price range. The 
    # high of the second day is lower than the first, and the low of the second 
    # is higher than the first.
    def isInsideBar(prev, curr):
        if curr.closedUp:
            if prev.closedUp:
                return True if (curr.open > prev.open and curr.close < prev.close) else False
            if prev.closedDown:
                return True if (curr.close < prev.open and curr.open > prev.close) else False
        elif curr.closedDown:
            if prev.closedUp:
                return True if (curr.open < prev.close and curr.close > prev.open) else False
            if prev.closedDown:
                return True if (curr.close > prev.close and curr.open < prev.open) else False
        else:
            False

    # Returns 1 for Bullish Engulfing, -1 for Bearish Engulfing, 0 for no engulfing pattern.
    #
    # A bullish engulfing pattern is a white candlestick that closes higher than the previous 
    # day's opening after opening lower than the previous day's close. It can be identified 
    # when a small black candlestick, showing a bearish trend, is followed the next day by a 
    # large white candlestick, showing a bullish trend, the body of which completely overlaps 
    # or engulfs the body of the previous day’s candlestick.
    def bullBearEngulfing(current, previous):

        currentDown = True if current.open - current.close > 0 else False
        currentUp = not currentDown
        prevDown = True if previous.open - previous.close > 0 else False
        prevUp = not prevDown

        if currentUp and prevDown:
            return 1 if current.open < previous.close and current.close > previous.open else 0
        elif currentDown and prevUp:
            return -1 if current.open > previous.close and current.close < previous.open else 0
        else: 
            return 0

    # Returns True if candle is a hammer candlestick, false otherwise
    #
    # A hammer is a price pattern in candlestick charting that occurs 
    # when a security trades significantly lower than its opening, but 
    # rallies within the period to close near opening price. This pattern 
    # forms a hammer-shaped candlestick, in which the lower shadow is at 
    # least twice the size of the real body. 
    def hammer(candle):
        if candle.closedUp:
            return True if ((candle.open - candle.low) >= candle.body * 2) and ((candle.open - candle.low) > (candle.high - candle.close)*2) else False
        elif candle.closedDown:
            return True if ((candle.close - candle.low) >= candle.body * 2) and ((candle.close - candle.low) > (candle.high - candle.open)*2) else False
        else:
            return False