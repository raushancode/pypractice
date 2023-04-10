import json
import requests
import sys

if len(sys.argv) == 2:
    try:
        arg = float(sys.argv[1])

    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # o = json.dumps(response.json(), indent=4)
    # print(o)
    o = response.json()
    # print(response.json())
    # print(json.dumps(response.json(), indent=4))
    rate = o["bpi"]["USD"]["rate_float"]
    amount = rate * arg
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("request exception")
    sys.exit(1)