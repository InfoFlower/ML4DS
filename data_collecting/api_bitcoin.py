#Fonction faites grâce à Chat GPT disponible sur VSCode, elle a été modifiée par la suite
#Prompt :
# "Use binance API to get the data of a given interval for a given symbol."
import requests
from datetime import datetime, timedelta

def get_historical_data(start_date, interval='1d', symbol='BTCUSDT'):
    url = "https://api.binance.com/api/v3/klines"
    end_date = datetime.now()
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    all_data = []

    while start_date < end_date:
        # Calculate the end time for the current request
        current_end_date = min(start_date + timedelta(days=1000), end_date)

        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': int(start_date.timestamp() * 1000),
            'endTime': int(current_end_date.timestamp() * 1000),
            'limit': 1000
        }
        response = requests.get(url, params=params)
        data = response.json()
        if not data:
            break
        all_data.extend(data)
        start_date = current_end_date

    return all_data