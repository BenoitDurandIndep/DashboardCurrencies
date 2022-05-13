from datetime import date, timedelta
from pprint import pprint
import requests

# SET PRIVATE KEY IN A CONF FILE LIKE DJANGO PRIVATE KEY


def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date-timedelta(days=days)

    req = requests.get(
        url=f"https://api.apilayer.com/exchangerates_data/history?start_at={start_date}&end_date={end_date}&symbols={','.join(currencies)}")
    if not req and not req.json():
        return False, False

    api_rates = req.json().get("rates")
    pprint(api_rates)
    return None, None


if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "EUR"])
