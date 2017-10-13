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
    myword=random.choice(lines)
    print(myword)
    dog_stuff = "<b>DOG FACTS!!!</b>\n\n" + myword
    
    yield from bot.coro_send_message(event.conv_id, dog_stuff)

def hackers (bot, event):
    lines = open('/home/sky/hangoutsbot/hangupsbot/plugins/hackers.txt').read().splitlines()
    myword=random.choice(lines)
    print(myword)
    dog_stuff = myword
    
    yield from bot.coro_send_message(event.conv_id, dog_stuff)

def rising(bot, event):
    url = 'http://www.fplstatistics.co.uk/Home/IndexWG'
    header = {'User-Agent': 'Mozilla/5.0'}

    r = urllib.request.Request(url=url, headers=header)
    page = urllib.request.urlopen(r)
    soup = BeautifulSoup(page.read(), "lxml")
    string = 'tbody tr:nth-of-type(1) td:nth-of-type(1), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(6), tbody tr:nth-of-type(2) td:nth-of-type(1), tbody tr:nth-of-type(2) td:nth-of-type(2), tbody tr:nth-of-type(2) td:nth-of-type(6), tbody tr:nth-of-type(3) td:nth-of-type(1), tbody tr:nth-of-type(3) td:nth-of-type(2), tbody tr:nth-of-type(3) td:nth-of-type(6), tbody tr:nth-of-type(4) td:nth-of-type(1), tbody tr:nth-of-type(4) td:nth-of-type(2), tbody tr:nth-of-type(4) td:nth-of-type(6)'
    data = soup.select(string)

    player1Name = data[0].contents[0].strip()
    player1Team = data[1].contents[0].strip()
    player1Price = data[2].contents[0].strip()

    player2Name = data[3].contents[0].strip()
    player2Team = data[4].contents[0].strip()
    player2Price = data[5].contents[0].strip()

    player3Name = data[6].contents[0].strip()
    player3Team = data[7].contents[0].strip()
    player3Price = data[8].contents[0].strip()

    fpl_strings1 = ["<b>"+player1Name+"</b>", player1Team, "<i>"+player1Price+"</i>"]
    fpl_strings2 = ["<b>"+player2Name+"</b>", player2Team, "<i>"+player2Price+"</i>"]
    fpl_strings3 = ["<b>"+player3Name+"</b>", player3Team, "<i>"+player3Price+"</i>"]

    # This will print to console
    print(" ".join(fpl_strings1))

    # This preps the strings for printing in Hangouts
    fpl_stuff = "<b>FPL Soon To Rise</b><br /><br />"+ " ".join(fpl_strings1)+"<br />"+ " ".join(fpl_strings2)+"<br />"+ " ".join(fpl_strings3)
    yield from bot.coro_send_message(event.conv_id, fpl_stuff)