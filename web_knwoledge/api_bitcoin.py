#Fonction faites grâce à Chat GPT disponible sur VSCode, elle a été modifiée par la suite
#Prompt :
# "Use binance API to get the data of a given interval for a given symbol."
import requests

def get_data(interval,symbol='BTCUSDT'):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': 1000
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data