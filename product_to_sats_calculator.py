#!/usr/bin/env python3
"""
This program calculates the price of a product in satoshis using an API from Coindesk. The program can be run on-the-go
on your mobile device to calculate the price of your products in real time.

Price, store title, price menu title, and product label can be edited as needed for your store. If you only need one
product, then comment out lines 42, 46, and 60-64.

Run this program on your phone with the following apps:
Android: https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=en_US&gl=US
iPhone: https://apps.apple.com/in/app/python3ide/id1357215444

Copy and paste the code here into the respective app or save the .py file and open it the given app.

See an example screenshot of the output here: https://i.postimg.cc/fRPdWTJM/sat-price-calc.jpg
"""

# Import modules.
from pip._vendor import requests  # This needs to be fixed. It should just be "import requests" but I cannot get it to
# to work.

import locale
locale.setlocale(locale.LC_ALL, '')

# Extract the bitcoin USD price from the API text and convert it to a float.
API_URL = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
btc_price_string = API_URL.text[372:383]  # Isolate USD price from API text; for example, price looks like '37762.7667'.
btc_price_usd = float(btc_price_string.replace(',', ''))  # Remove comma from price string and convert the price to a
# float; includes four decimal places.

# Display dividers, title, and bitcoin price USD.
store_title = "Heady Tie Dyes"  # Set the title of the store; This can be replaced with any name.
print("=" * 25)  # Divider.
print(store_title.center(25))  # Display centered title.
print("=" * 25)  # Divider.
price_str_rounded = API_URL.text[372:381]  # Bitcoin price in USD rounded to two decimal places.
print(("1 BTC = $" + price_str_rounded).center(25))
print("=" * 25)  # Divider.

# Set the price of the product in USD.
product_one_price_usd = 15  # These prices can be adjusted.
product_two_price_usd = 25  # If you only need one product, then comment out line 42.

# Calculate the product price in satoshis for each product.
product_one_price_sats = (product_one_price_usd / btc_price_usd) * 100000000  # Calculate price per product in bitcoin.
product_two_price_sats = (product_two_price_usd / btc_price_usd) * 100000000  # If you only need one product, then
# comment out line 46.

# Display menu title and divider.
menu_title = "Menu"  # Menu title; this can be adjusted.
print(menu_title.center(25))  # Display price menu title.
print("=" * 25)  # Divider.

# Format product one label and display it.
product_one_label = "Standard" + " = "  # Product one label; this label can be changed.
product_one_price_label = format(round(product_one_price_sats), ',') + " sats"  # Set price in sats with units.
print((product_one_label + product_one_price_label).center(25))  # Display product label and price in sats.

# Format product two label and display it.
product_two_label = "Top-shelf" + " = "  # Product two label; this label can be changed; comment out lines 60-64 if you
# do not need a second product.

product_two_price_label = format(round(product_two_price_sats), ',') + " sats"  # Set price in sats with units.
print((product_two_label + product_two_price_label).center(25))  # Display product label and price in sats.

# Divider and goodbye.
print("=" * 25)  # Divider.
print("Thank you!".center(25))  # Goodbye message.
