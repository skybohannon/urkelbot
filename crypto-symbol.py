import urllib.request
import json

urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=0"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
crypto_list = json.loads(data.decode(encoding))

def symbol(sym):

    for coin in crypto_list:

        if coin["symbol"] == sym.upper():
            coin_name = coin["name"]
            usd_price = float(coin["price_usd"])
            btc_price = float(coin["price_btc"])
            change_24h = float(coin["percent_change_24h"])
            change_1h = float(coin["percent_change_1h"])

    symbol_output = "<b>" + coin_name + " (" + sym.upper() + ")</b>\n\n<b>USD</b>: ${:,.3f}\n"\
        "<b>BTC</b>: {:.7f}\n"\
        "<b>24H Change</b>: {:+.2f}%\n"\
        "<b>1H Change</b>: {:+.2f}%"\
        .format(usd_price, btc_price, change_1h, change_24h)

    return symbol_output


print(symbol("aaa"))