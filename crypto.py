import urllib.request
import json

urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=0"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
crypto_list = json.loads(data.decode(encoding))

for coin in crypto_list:
    if coin["id"] == "bitcoin":
        btc_price = float(coin["price_usd"])
    elif coin["id"] == "bitcoin-cash":
        bch_price = float(coin["price_usd"])
    elif coin["id"] == "ethereum":
        eth_price = float(coin["price_usd"])
    elif coin["id"] == "icon":
        icx_price = float(coin["price_usd"])
    elif coin["id"] == "litecoin":
        ltc_price = float(coin["price_usd"])
    elif coin["id"] == "nxt":
        nxt_price = float(coin["price_usd"])
    elif coin["id"] == "stellar":
        xlm_price = float(coin["price_usd"])
    elif coin["id"] == "raiblocks":
        xrb_price = float(coin["price_usd"])

crypto_output = "<b>BTC</b>: ${:,.2f}\n<b>BCH</b>: ${:,.2f}\n<b>ETH</b>: ${:,.2f}\n<b>ICX</b>: ${:,.2f}\n<b>LTC</b>: " \
                "${:,.2f}\n<b>NXT</b>: ${:,.2f}\n<b>XLM</b>: ${:,.3f}\n<b>XRB</b>: ${:,.2f}"\
                .format(btc_price, bch_price, eth_price, icx_price, ltc_price, nxt_price, xlm_price, xrb_price)

print(crypto_output)