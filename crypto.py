import urllib.request
import json

urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=30"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
crypto_list = json.loads(data.decode(encoding))

for coin in crypto_list:
    if coin["symbol"] == "BTC":
        btc_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "ETH":
        eth_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "BCH":
        bch_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "LTC":
        ltc_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "XLM":
        xlm_price = round(float(coin["price_usd"]), 3)
    elif coin["symbol"] == "NXT":
        nxt_price = round(float(coin["price_usd"]), 2)
    elif coin["symbol"] == "XRP":
        xrp_price = round(float(coin["price_usd"]), 2)


crypto_output = "<b>BTC</b>: ${}\n<b>BCH</b>: ${}\n<b>ETH</b>: ${}\n<b>LTC</b>: ${}\n<b>XLM</b>: ${}\n<b>NXT</b>: ${}\n<b>XRP</b>: ${}".format(btc_price, bch_price, eth_price, ltc_price, xlm_price, nxt_price, xrp_price)

print(crypto_output)