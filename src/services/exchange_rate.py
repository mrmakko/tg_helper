import requests

def get_baht_to_ruble() -> str:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/THB")
    data = response.json()
    rate = data["rates"]["RUB"]
    adjusted_rate = round(rate * 1.10 / 0.05) * 0.05
    return f'{adjusted_rate:.2f} (исходный курс: {rate})'

def get_usdt_to_baht() -> str:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USDT")
    data = response.json()
    rate = data["rates"]["THB"]
    adjusted_rate = round(rate * 0.975 / 0.05) * 0.05
    return f'{adjusted_rate:.2f} (исходный курс: {rate})'