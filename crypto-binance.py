from binance.client import Client

with open("binance-api.txt", "r") as api_key:
    api_key = api_key.read()

with open("binance-secret.txt", "r") as api_secret:
    api_secret = api_secret.read()

client = Client(api_key, api_secret)
info = client.get_account()
balance = client.get_asset_balance(asset="BTC")
balance_output = "<b>Binance balances</b>: \n\n"
for balances in info["balances"]:
    if float(balances["free"]) > 0.25:
        balance_output = balance_output + "<b>{}</b>: {:.2f}\n".format(balances["asset"], float(balances["free"]))


print(balance_output)