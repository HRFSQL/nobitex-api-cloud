import requests

# Binance API endpoint for Bitcoin price in EUR
url = "https://api.binance.com/api/v3/ticker/price"
params = {
    'symbol': 'BTCEUR'
}

response = requests.get(url, params=params)
data = response.json()

# Get Bitcoin price in EUR
bitcoin_price_eur = data['price']
print(f"Bitcoin (BTC) Price: €{bitcoin_price_eur}")
