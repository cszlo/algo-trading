import json
import requests
import pprint as pp
import time
# import termcolor

OPEN = 'open'
HIGH = 'high'
LOW = 'low'
CLOSE = 'close'
INSIDE_BAR = 'insideBar'

class bcolors:
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

data = []

klines = {}

# url = 'https://api.binance.us/api/v3/klines?symbol=BTCUSD&interval=1d&limit=1000'
url = 'https://api.binance.us/api/v3/order?symbol=BTCUSD'  
h = {'apiKey' : '5yBfTcNLDzwQBCECfhonTS17GolOqrOUD78CwkmuTJZMeXYYO6DccnpNr5WmiKBI'}
response = requests.get(f'{url}', headers = h)

pp.pprint(response.content)

# pp.pprint(json.loads(response.content))

# def upDown(data, index):
#     if data[index][1] > data[index][4]:
#         return -1
#     elif  data[index][1] < data[index][4]:
#         return 1
#     else:
#         return 0

# def isInsideBar(data, index):
#     if index < 1:
#         return False

#     thisOpen= data[index][1]
#     thisClose = data[index][4]
#     thisDown = True if float(thisOpen) - float(thisClose) > 0 else False
#     thisUp = not thisDown
#     prevOpen = data[index-1][1]
#     prevClose = data[index-1][4]
#     prevDown = True if float(prevOpen) - float(prevClose) > 0 else False
#     prevUp = not prevDown

#     if thisUp and prevUp:
#         return True if float(thisOpen) > float(prevOpen) and float(thisClose) < float(prevClose) else False
#     if thisUp and prevDown:
#         return True if float(thisOpen) > float(prevClose) and float(thisClose) < float(prevOpen) else False
#     if thisDown and prevUp:
#         return True if float(thisOpen) < float(prevClose) and float(thisClose) > float(prevOpen) else False
#     if thisDown and prevDown:
#         return True if float(prevOpen) > float(thisOpen) and float(prevClose) < float(thisClose) else False

# # Load response to array
# for i in range(len(response)):
#     data.append({'timestamp' : response[i][0],
#                  'open' : response[i][1],
#                  'high' : response[i][2],
#                  'low'  : response[i][3],
#                  'close': response[i][4],
#                  'insideBar' : isInsideBar(response, i)
#                 })
    
# print(time.ctime(data[0]['timestamp']/1000))

# # iterate over response data
# profit = 0.0
# for i in range(len(data)):
#     if data[i][INSIDE_BAR] == True and data[i-1][INSIDE_BAR] == True:
#         # print(time.ctime(data[i]['timestamp']/1000))
#         profit += float(data[i+1]['close']) - float(data[i+1]['open'])
#         # percentage change of following bar
#         print(((float(data[i+1]['close'])/float(data[i+1]['open']))*100)-100)
# print(profit)
        