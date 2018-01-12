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
        btc_change = float(coin["percent_change_24h"])
    elif coin["id"] == "bitcoin-cash":
        bch_price = float(coin["price_usd"])
        bch_change = float(coin["percent_change_24h"])
    elif coin["id"] == "ethereum":
        eth_price = float(coin["price_usd"])
        eth_change = float(coin["percent_change_24h"])
    elif coin["id"] == "icon":
        icx_price = float(coin["price_usd"])
        icx_change = float(coin["percent_change_24h"])
    elif coin["id"] == "litecoin":
        ltc_price = float(coin["price_usd"])
        ltc_change = float(coin["percent_change_24h"])
    elif coin["id"] == "stellar":
        xlm_price = float(coin["price_usd"])
        xlm_change = float(coin["percent_change_24h"])
    elif coin["id"] == "raiblocks":
        xrb_price = float(coin["price_usd"])
        xrb_change = float(coin["percent_change_24h"])
    elif coin["id"] == "request-network":
        req_price = float(coin["price_usd"])
        req_change = float(coin["percent_change_24h"])
    elif coin["id"] == "ripple":
        xrp_price = float(coin["price_usd"])
        xrp_change = float(coin["percent_change_24h"])
    elif coin["id"] == "vechain":
        ven_price = float(coin["price_usd"])
        ven_change = float(coin["percent_change_24h"])
    elif coin["id"] == "binance-coin":
        bnb_price = float(coin["price_usd"])
        bnb_change = float(coin["percent_change_24h"])

crypto_output = "<b>BTC</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>BCH</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>ETH</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>LTC</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>BNB</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>ICX</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>REQ</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>VEN</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>XLM</b>: ${:,.3f}  (<i>{:+.2f}%</i>)\n" \
                "<b>XRB</b>: ${:,.2f}  (<i>{:+.2f}%</i>)\n" \
                "<b>XRP</b>: ${:,.2f}  (<i>{:+.2f}%</i>)" \
                .format(btc_price, btc_change, bch_price, bch_change, eth_price, eth_change, ltc_price, ltc_change, bnb_price, bnb_change, icx_price, icx_change, req_price, req_change, ven_price, ven_change, xlm_price, xlm_change, xrb_price, xrb_change, xrp_price, xrp_change)

print(crypto_output)