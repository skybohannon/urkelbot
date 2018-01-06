import urllib.request
import json

urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=0"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
crypto_list = json.loads(data.decode(encoding))

def symbol(s):
    price = ""
    for coin in crypto_list:

        if coin["symbol"] == s.upper():
            price = float(coin["price_usd"])

    return "<b>" + s.upper() + "</b>: ${:,.2f}".format(price)

print(symbol("bnty"))
