#!/usr/bin/env python3

from pip._vendor import requests
import locale
locale.setlocale(locale.LC_ALL, '')


url = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
price_str = url.text[18:23]
btc_price = int(price_str)

print("http://HeadyTieDyes.com/")
print("Bitcoin = " + locale.currency(btc_price, grouping=True))

price_usd = 15

two_price = 25

price_sats = (price_usd / btc_price) * 100000000

two_for = (two_price / btc_price) * 100000000

print("1 shirt for", format(round(price_sats), ','), "sats")

print("2 shirts for", format(round(two_for), ','), "sats")

