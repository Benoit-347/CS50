import sys, requests

try:             # taking input of number of bitcoins (to check the price of total)
    num_bitcoin = sys.argv[1]
    num_bitcoin = float(num_bitcoin)
except:
    sys.exit("Enter decimal in command line input")

# obtaining current price of bitcoin by first obtaining json file
try:
    api_json = requests.get("https://api.coincap.io/v2/assets/bitcoin").json()
except requests.RequestException:
    print("Error getting json object")
    sys.exit()

price = float(api_json["data"]["priceUsd"])     # obtaining price from json file

total = num_bitcoin * price     #calc total price

print(f"${total:,.4f}")     # prints total price formatted to 4 decimal places with comma every 3 digits
