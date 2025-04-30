import os
import requests
import psycopg2
from datetime import datetime

# Load environment variables
db_url = os.environ['DATABASE_URL']

# Example Nobitex API endpoint (adjust as needed)
response = requests.get("https://api.nobitex.ir/market/stats")
data = response.json()

# Example of inserting price data (adapt field names as needed)
conn = psycopg2.connect(db_url)
cursor = conn.cursor()

# Just an example - replace with real fields & logic
price = data['stats']['btc-irt']['latest']
cursor.execute("INSERT INTO btc_prices (price, collected_at) VALUES (%s, %s)", (price, datetime.utcnow()))

conn.commit()
cursor.close()
conn.close()
