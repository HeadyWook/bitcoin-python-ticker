#!/usr/bin/env python3
"""
This program calculates the price of a product in bitcoin (satoshis) using an API from Coindesk. It can be run on-the-go
 on a mobile device to calculate the price of a product(s) on demand.

Price, store title, menu title, and product label can each be edited as needed for any store product. Two products are
listed in this program. Comment out lines 40, 44, and 56-59 if a second product is not needed. If more products are
desired, then copy and paste lines 40, 44, and 56-59 directly below each respective one and update the product numbers.

Run this program on a mobile phone with the following apps:
Android: https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=en_US&gl=US
iPhone: https://apps.apple.com/in/app/python3ide/id1357215444

Copy and paste the code in 'product_to_sats_calculator.py' to app or download the .py file and open it in the app.

See an example screenshot of the output here: https://i.postimg.cc/fRPdWTJM/sat-price-calc.jpg
"""

# Import modules.
from pip._vendor import requests  # This needs to be fixed. It should just be "import requests" but I cannot get it to
# to work.

# Extract the bitcoin USD price from the API text and convert it to a float.
api_url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
btc_usd_string = api_url.text[372:383]  # Isolate USD price from API text; for example, price looks like '37762.7667'.
btc_usd = float(btc_usd_string.replace(',', ''))  # Remove comma from price string and convert the price to a
# float; includes four decimal places for more precision.

# Display dividers, title, and bitcoin price in USD.
main_title = "Heady Tie Dyes"  # Set the title of the store; The text within the quotes can be edited as needed.
print("=" * 25)  # Divider.
print(main_title.center(25))  # Display centered title.
print("=" * 25)  # Divider.
btc_usd_rounded = str(format(round(btc_usd, 2), ','))  # Round two decimal places, format, and make string.
print(("1 BTC = $" + btc_usd_rounded).center(25))  # Display Bitcoin in USD.
print("=" * 25)  # Divider.

# Set the price of the product in USD.
product_1_usd = 15.00  # The price can be edited as needed.
product_2_usd = 25.00  # The price can be edited as needed.

# Calculate the products price in satoshis.
product_1_sats = (product_1_usd / btc_usd) * 100000000  # Convert from BTC to sats.
product_2_sats = (product_2_usd / btc_usd) * 100000000  # Convert from BTC to sats.

# Display menu title and divider.
menu_title = "Menu"  # Menu title; this can be adjusted.
print(menu_title.center(25))  # Display price menu title.
print("=" * 25)  # Divider.

# Format product 1 label and display it.
product_1_label = "Standard" + " = "  # Product 1 label; The text within the "Standard" quote can be edited as needed.
product_1_price_label = format(round(product_1_sats), ',') + " sats"  # Round price and format in sats.
print((product_1_label + product_1_price_label).center(25))  # Display product label and price in sats.

# Format product 2 label and display it.
product_2_label = "Top-shelf" + " = "  # Product 2 label; The text within the "Top-shelf" quote can be edited as needed.
product_2_price_label = format(round(product_2_sats), ',') + " sats"  # Round price and format in sats.
print((product_2_label + product_2_price_label).center(25))  # Display product label and price in sats.

# Divider and goodbye.
print("=" * 25)  # Divider.
print("Thank you!".center(25))  # Goodbye message.
