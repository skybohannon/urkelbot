import urllib.request
import json

urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=0"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
crypto_list = json.loads(data.decode(encoding))

for coin in crypto_list:
    if coin["symbol"] == "BTC":
        btc_price = float(coin["price_usd"])
    elif coin["symbol"] == "BCH":
        bch_price = float(coin["price_usd"])
    elif coin["symbol"] == "ETH":
        eth_price = float(coin["price_usd"])
    elif coin["symbol"] == "ICX":
        icx_price = float(coin["price_usd"])
    elif coin["symbol"] == "LTC":
        ltc_price = float(coin["price_usd"])
    elif coin["symbol"] == "NXT":
        nxt_price = float(coin["price_usd"])
    elif coin["symbol"] == "XLM":
        xlm_price = float(coin["price_usd"])
    elif coin["symbol"] == "XRB":
        xrb_price = float(coin["price_usd"])

crypto_output = "<b>BTC</b>: ${:,.2f}\n<b>BCH</b>: ${:,.2f}\n<b>ETH</b>: ${:,.2f}\n<b>ICX</b>: ${:,.2f}\n<b>LTC</b>: " \
                "${:,.2f}\n<b>NXT</b>: ${:,.2f}\n<b>XLM</b>: ${:,.3f}\n<b>XRB</b>: ${:,.2f}"\
                .format(btc_price, bch_price, eth_price, icx_price, ltc_price, nxt_price, xlm_price, xrb_price)

print(crypto_output)