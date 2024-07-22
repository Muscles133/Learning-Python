import requests
import sys

site = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    r = requests.get(site)
    data = r.json()
    #print(r.text[:500])

    # for key, value in r.headers.items():
    #             print(f"{key}: {value}")

    usd_float_rate = data['bpi']['USD']['rate_float']
    print(f"Current Bitcoin price: ${usd_float_rate:.4f}")

except requests.RequestException:
    sys.exit()