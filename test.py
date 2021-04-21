import requests

url = "https://ftx.com/api/markets/{}/candles?resolution={}".format("SHIT-PERP", 86400)
data = requests.get(url)
data = data.json()['result']
data.reverse()

weekly_data = data[0:31]
weekly_data.reverse()
week_open = weekly_data[0]['open']
week_close = weekly_data[30]['close']

shit_percent_change = ((week_close - week_open) / week_open) * 100

url = "https://ftx.com/api/markets/{}/candles?resolution={}".format("ALT-PERP", 86400)
data = requests.get(url)
data = data.json()['result']
data.reverse()

weekly_data = data[0:31]
weekly_data.reverse()
week_open = weekly_data[0]['open']
week_close = weekly_data[30]['close']

alt_percent_change = ((week_close - week_open) / week_open) * 100
