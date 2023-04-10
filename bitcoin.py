import requests
import sys

# Get the number of bitcoins to buy from the command line arguments
try:
    num_bitcoins = float(sys.argv[1])
except (IndexError, ValueError):
    print("Error: Please enter a valid number of bitcoins.")
    sys.exit()

# Query the API for the current bitcoin price
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()  # Raises an exception if the response status code is not 200
    bitcoin_data = response.json()
    current_price = bitcoin_data['bpi']['USD']['rate_float']
except (requests.RequestException, KeyError):
    print("Error: Unable to retrieve current bitcoin price.")
    sys.exit()

# Calculate the cost of buying num_bitcoins
cost = num_bitcoins * current_price

# Output the result
print(f"Cost of buying {num_bitcoins:.8g} Bitcoins: ${cost:,.4f}")
