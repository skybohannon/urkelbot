"""
urkelbot
           _________._____ /\__.____.
           \    ___/     //   /_   / \_
         __ \\__   /   _/ \____/__,   /
   _____/__________\___\____ / /_    /
   \     _/__._______\   ___/_.__\  /_._______._______._______.________
   /    _    \  __   //       \___\/   \_   _  \_   _  \_  __  \_   _  \_
  /    _/    /  \   _/    /  _/   _/    /   /   /   /   /  \    /   /   /
  \____\____/\\_____\____/___\  ______//___/___/___/___/\\_____/___/___/
                              \/
"""
from __future__ import print_function
import plugins
import random
import re
import subprocess
import urllib.parse
from bs4 import BeautifulSoup


def _initialize(bot):
    plugins.register_user_command(["uptime"])
    plugins.register_user_command(["rising"])
    plugins.register_user_command(["standings"])
    plugins.register_user_command(["dogfacts"])
    plugins.register_user_command(["catfacts"])
    plugins.register_user_command(["hackers"])
    plugins.register_user_command(["bch"])
    plugins.register_user_command(["eth"])
    plugins.register_user_command(["crypto"])

def uptime(bot, event):
    proc1 = subprocess.check_output(['uptime']).decode('utf-8').strip("\n")
    time = re.search(r'up (.* days)?', proc1)
    proc2 = subprocess.check_output(['uptime', '-p']).decode('utf-8').strip("\n")
    time_pretty = re.search(r'up (.*)?', proc2)
    if time.group(1) is not None:
        time_strings = [time_pretty.group(1), "(" + time.group(1) + ")"]
        time_stuff = " ".join(time_strings)
    else:
        time_strings = [time_pretty.group(1)]
        time_stuff = " ".join(time_strings)
    yield from bot.coro_send_message(event.conv_id, time_stuff)

def dogfacts (bot, event):
    lines = open('/home/sky/hangoutsbot/hangupsbot/plugins/dogfacts.txt','r').read().splitlines()
    dogFact=random.choice(lines)
    print(dogFact)
    dogFactAll = "<b>DOG FACTS!!!</b>\n\n" + dogFact
    
    yield from bot.coro_send_message(event.conv_id, dogFactAll)

def catfacts(bot, event):
    catFact = "<b>CAT FACTS!!!</b>\n\n" + "Cats are stupid"
    yield from bot.coro_send_message(event.conv_id, catFact)

def hackers (bot, event):
    lines = open('/home/sky/hangoutsbot/hangupsbot/plugins/hackers.txt','r').read().splitlines()
    hackersQuote=random.choice(lines)
    print(hackersQuote)
    
    yield from bot.coro_send_message(event.conv_id, hackersQuote)

def rising(bot, event):
    url = 'http://www.fplstatistics.co.uk/Home/IndexWG'
    header = {'User-Agent': 'Mozilla/5.0'}

    r = urllib.request.Request(url=url, headers=header)
    page = urllib.request.urlopen(r)
    soup = BeautifulSoup(page.read(), "lxml")
    string = 'tbody tr:nth-of-type(1) td:nth-of-type(1), tbody tr:nth-of-type(1) td:nth-of-type(2), \
    tbody tr:nth-of-type(1) td:nth-of-type(6), tbody tr:nth-of-type(2) td:nth-of-type(1), tbody tr:nth-of-type(2) \
    td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(6), tbody tr:nth-of-type(3) td:nth-of-type(1), \
    tbody tr:nth-of-type(3) td:nth-of-type(2), tbody tr:nth-of-type(3) td:nth-of-type(6), tbody tr:nth-of-type(4) \
    td:nth-of-type(1), tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(6)'
    data = soup.select(string)
    player1Name = data[0].text.strip()
    player1Team = data[1].text.strip()
    player1Price = data[2].text.strip()
    player2Name = data[3].text.strip()
    player2Team = data[4].text.strip()
    player2Price = data[5].text.strip()
    player3Name = data[6].text.strip()
    player3Team = data[7].text.strip()
    player3Price = data[8].text.strip()

    lineup = {
        1: {"playerName": player1Name,
            "playerTeam": player1Team,
            "playerPrice": player1Price},
        2: {"playerName": player2Name,
            "playerTeam": player2Team,
            "playerPrice": player2Price},
        3: {"playerName": player3Name,
            "playerTeam": player3Team,
            "playerPrice": player3Price},
    }

    player1 = '<b>' + lineup[1]["playerName"] + '</b> ' + lineup[1]["playerTeam"] + ' <i>' + lineup[1][
        "playerPrice"] + '</i><br />'
    player2 = '<b>' + lineup[2]["playerName"] + '</b> ' + lineup[2]["playerTeam"] + ' <i>' + lineup[2][
        "playerPrice"] + '</i><br />'
    player3 = '<b>' + lineup[3]["playerName"] + '</b> ' + lineup[3]["playerTeam"] + ' <i>' + lineup[3][
        "playerPrice"] + '</i>'

    risingOutput = '<b>FPL Soon To Rise</b><br /><br />' + ''.join(player1) + ''.join(player2) + ''.join(player3)
    yield from bot.coro_send_message(event.conv_id, risingOutput)

def standings(bot, event):
    import urllib.request
    from bs4 import BeautifulSoup

    url = 'https://fplmystats.com/league/116940/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    string = 'tbody tr:nth-of-type(1) td:nth-of-type(2), \
            tbody tr:nth-of-type(2) td:nth-of-type(2), \
            tbody tr:nth-of-type(3) td:nth-of-type(2), \
            tbody tr:nth-of-type(4) td:nth-of-type(2), \
            tbody tr:nth-of-type(5) td:nth-of-type(2), \
            tbody tr:nth-of-type(6) td:nth-of-type(2), \
            tbody tr:nth-of-type(7) td:nth-of-type(2), \
            tbody tr:nth-of-type(8) td:nth-of-type(2), \
            tbody tr:nth-of-type(9) td:nth-of-type(2), \
            tbody tr:nth-of-type(10) td:nth-of-type(2), \
            tbody tr:nth-of-type(11) td:nth-of-type(2), \
            tbody tr:nth-of-type(12) td:nth-of-type(2)'

    data = soup.select(string)
    print(data)

    team1Owner = data[0].text.strip()
    team2Owner = data[1].text.strip()
    team3Owner = data[2].text.strip()
    team4Owner = data[3].text.strip()
    team5Owner = data[4].text.strip()
    team6Owner = data[5].text.strip()
    team7Owner = data[6].text.strip()
    team8Owner = data[7].text.strip()
    team9Owner = data[8].text.strip()
    team10Owner = data[9].text.strip()
    team11Owner = data[10].text.strip()
    team12Owner = data[11].text.strip()

    top = {
        1: {"teamName": team1Owner},
        2: {"teamName": team2Owner},
        3: {"teamName": team3Owner},
        4: {"teamName": team4Owner},
        5: {"teamName": team5Owner},
        6: {"teamName": team6Owner},
        7: {"teamName": team7Owner},
        8: {"teamName": team8Owner},
        9: {"teamName": team9Owner},
        10: {"teamName": team10Owner},
        11: {"teamName": team11Owner},
        12: {"teamName": team12Owner}
    }

    loc = 1
    while loc <= 12:
        globals()['team%s' % loc] = str(loc) + '. <b>' + top[loc]["teamName"] + '</b>'
        loc += 1

    topOutput = '<b>FPL Standings</b><br /><br />' + ''.join(team1) + '<br/>' + ''.join(team2) + '<br/>' + ''.join(
        team3) + '<br/>' + ''.join(team4) + '<br/>' + ''.join(team5) + '<br/>' + ''.join(team6) + '<br/>' + ''.join(
        team7) + '<br/>' + ''.join(team8) + '<br/>' + ''.join(team9) + '<br/>' + ''.join(team10) + '<br/>' + ''.join(
        team11) + '<br/>' + ''.join(team12)
    print(topOutput)
    yield from bot.coro_send_message(event.conv_id, topOutput)


def bch(bot, event):
    import urllib.request
    from bs4 import BeautifulSoup

    url = 'https://coinmarketcap.com/currencies/bitcoin-cash/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    string = '#quote_price'

    data = soup.select(string)
    stripped = data[0].text.strip()

    bchOutput = str(stripped)
    print(bchOutput)
    yield from bot.coro_send_message(event.conv_id, bchOutput)

def eth(bot, event):
    import urllib.request
    from bs4 import BeautifulSoup

    url = 'https://coinmarketcap.com/currencies/ethereum/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    string = '#quote_price'

    data = soup.select(string)
    stripped = data[0].text.strip()

    ethOutput = str(stripped)


    print(ethOutput)
    yield from bot.coro_send_message(event.conv_id, ethOutput)

def crypto(bot, event):
    import urllib.request
    from bs4 import BeautifulSoup

    url = 'https://coinmarketcap.com/currencies/ethereum/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    string = '#quote_price'

    data = soup.select(string)
    stripped = data[0].text.strip()

    ethOutput = str(stripped)

    url = 'https://coinmarketcap.com/currencies/bitcoin-cash/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    string = '#quote_price'

    data = soup.select(string)
    stripped = data[0].text.strip()

    bchOutput = str(stripped)

    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    string = '#quote_price'

    data = soup.select(string)
    stripped = data[0].text.strip()

    btcOutput = str(stripped)

    allOutput = "BTC: " + btcOutput + "\nBCH: " + bchOutput + "\nETH: " + ethOutput
    yield from bot.coro_send_message(event.conv_id, allOutput)