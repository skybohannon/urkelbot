import urllib.request
import json

urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=5"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
crypto_list = json.loads(data.decode(encoding))

for coin in crypto_list:
    if coin["symbol"] == "BTC":
        btc_price = coin["price_usd"]
    elif coin["symbol"] == "ETH":
        eth_price = coin["price_usd"]
    elif coin["symbol"] == "BCH":
        bch_price = coin["price_usd"]

print("<b>BTC</b>: ${}\n<b>BCH</b>: ${}\n<b>ETH</b>: ${}".format(btc_price, bch_price, eth_price))