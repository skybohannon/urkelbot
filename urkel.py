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
    plugins.register_user_command(["dogfacts"])
    plugins.register_user_command(["catfacts"])
    plugins.register_user_command(["hackers"])

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
    lines = open('/home/sky/hangoutsbot/hangupsbot/plugins/dogfacts.txt').read().splitlines()
    dogFact=random.choice(lines)
    print(dogFact)
    dogFactAll = "<b>DOG FACTS!!!</b>\n\n" + dogFact
    
    yield from bot.coro_send_message(event.conv_id, dogFactAll)

def catfacts(bot, event):
    catFact = "<b>CAT FACTS!!!</b>\n\n" + "Cats are stupid"
    yield from bot.coro_send_message(event.conv_id, catFact)

def hackers (bot, event):
    lines = open('/home/sky/hangoutsbot/hangupsbot/plugins/hackers.txt').read().splitlines()
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