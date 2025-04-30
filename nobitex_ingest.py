import requests
import psycopg2
from datetime import datetime

# Replace with your actual Neon PostgreSQL connection info
conn = psycopg2.connect(
    host="your_neon_host",
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    sslmode="require"
)

cursor = conn.cursor()

# Fetch crypto data from CoinGecko
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'eur',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
}
response = requests.get(url, params=params)
data = response.json()

# Insert or update rows
for coin in data:
    cursor.execute("""
        INSERT INTO cryptos (id, name, symbol, price_eur, market_cap, last_updated)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE
        SET price_eur = EXCLUDED.price_eur,
            market_cap = EXCLUDED.market_cap,
            last_updated = EXCLUDED.last_updated;
    """, (
        coin["id"],
        coin["name"],
        coin["symbol"],
        coin["current_price"],
        coin["market_cap"],
        datetime.strptime(coin["last_updated"], "%Y-%m-%dT%H:%M:%S.%fZ")
    ))

# Commit and close
conn.commit()
cursor.close()
conn.close()
print("✅ Data stored successfully.")
