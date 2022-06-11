from datetime import date, timedelta
from pprint import pprint
import requests
from decouple import config

API_LAYER_KEY = config("API_LAYER_KEY")


def get_rates(currencies, base="EUR", days=30):

    end_date = date.today()
    start_date = end_date-timedelta(days=days)
    base_url_api = "https://api.apilayer.com/exchangerates_data/timeseries?"
    payload = {}
    headers = {
        "apikey": API_LAYER_KEY
    }

    req = requests.get(
        url=f"{base_url_api}base={base}&start_date={start_date}&end_date={end_date}&symbols={','.join(currencies)}", headers=headers, data=payload)

    if not req and not req.json():
        return False, False

    print(f"statut={req.status_code}")

    api_rates = req.json().get("rates")

    all_rates = {currency: []
                 for currency in currencies}  # get currencies in a dictionnay
    all_days = sorted(api_rates.keys())

    for each_day in all_days:
        # print(api_rates.get(each_day))
        # add rates in the dictionnary
        [all_rates[currency].append(rate)
         for currency, rate in api_rates[each_day].items()]

    #pprint(all_rates)

    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"], base="EUR")
    pprint(days)
    pprint(rates)
