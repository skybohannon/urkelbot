import binance

with open("binance-api.txt", "r") as api_key:
    key = apikey.read()

with open("binance-secret.txt", "r") as api_secret:
    key = apikey.read()

binance.set(api_key, api_secret)

print(binance.myTrades("BNBBTC"))