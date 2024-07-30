import requests
import sys

site = "https://api.coindesk.com/v1/bpi/currentprice.json"          #website to scape
usd_amount = float(sys.argv[1])                                     #takes the command line arg as the usd amount

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")                               #code only works if there is an arg in the command line

    # elif usd_amount.isdigit() == False:
    #     sys.exit("Command-line argument is not a number ")                              #code needs to be a digit

    else:
        r = requests.get(site)
        data = r.json()
        usd_float_rate = data['bpi']['USD']['rate_float']
        result = usd_amount * usd_float_rate
        print(f"${result:,.4f}")

except requests.RequestException:
    sys.exit()

except ValueError:
    sys.exit("Command-line argument is not a number ")


