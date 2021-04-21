"""
Shows the weekly percent change of a given trading account and btc, eth, altcoin index, and shitcoin index as benchmarks.
"""
import pandas
import matplotlib.pyplot as plt
import requests

week_start_balance = 12000

# get pnl data from FTX csv file
df = pandas.read_csv("pnl.csv")
df = df[::-1].reset_index(drop=True) # reverse dataframe
total_pnl = float(df['total'].iloc[0])
acct_gain = float(total_pnl / week_start_balance) * 100

# get benchmark data
btc = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin").json()
btc = btc['market_data']["price_change_percentage_7d"]

eth = requests.get("https://api.coingecko.com/api/v3/coins/ethereum").json()
eth = eth['market_data']["price_change_percentage_7d"]

url = "https://ftx.com/api/markets/{}/candles?resolution={}".format("SHIT-PERP", 86400)
data = requests.get(url)
data = data.json()['result']
data.reverse()

weekly_data = data[0:7]
weekly_data.reverse()
week_open = weekly_data[0]['open']
week_close = weekly_data[6]['close']

shit_percent_change = ((week_close - week_open) / week_open) * 100

url = "https://ftx.com/api/markets/{}/candles?resolution={}".format("ALT-PERP", 86400)
data = requests.get(url)
data = data.json()['result']
data.reverse()

weekly_data = data[0:7]
weekly_data.reverse()
week_open = weekly_data[0]['open']
week_close = weekly_data[6]['close']

alt_percent_change = ((week_close - week_open) / week_open) * 100

btc_eth_weighted_mean = (eth*0.4) + (btc*0.6)

# configure chart
fig, ax = plt.subplots()

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_title("7 Day Percent Change of Trading Account & Benchmarks")
ax.set_ylabel("Percent Change")
ax.set_xticklabels(('Account Balance', 'Bitcoin', 'Ethereum', '60:40 Bitcoin Ethereum Portfolio', 'Altcoin Index', 'Shitcoin Index'))

assets = ['Account Balance', 'Bitcoin', 'Ethereum', '60:40 Bitcoin Ethereum Portfolio', 'Altcoin Index', 'Shitcoin Index']
values = [acct_gain, btc, eth, btc_eth_weighted_mean, alt_percent_change, shit_percent_change]

ax.bar(assets,values)

plt.show()