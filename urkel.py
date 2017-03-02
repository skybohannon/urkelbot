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

import plugins
import requests
import re
import subprocess
import urllib.parse
from bs4 import BeautifulSoup
from datetime import date
import json
import io
import os
import aiohttp

def _initialize(bot):
    plugins.register_user_command(["fpl"])
    plugins.register_user_command(["players"])
    plugins.register_user_command(["uptime"])

def fpl(bot, event, *args):
    if "ping" in args:
        ping_stuff = ping()
        yield from bot.coro_send_message(event.conv_id, ping_stuff)
    else:
        server_stuff = get_status()
        yield from bot.coro_send_message(event.conv_id, server_stuff)


def players(bot, event, *args):
    players = get_status(players=True)
    yield from bot.coro_send_message(event.conv_id, players)


def uptime(bot, event, *args):
    proc = subprocess.check_output(['uptime']).decode('utf-8')
    time = re.search(r'up (.*?),', proc)
    proc2 = subprocess.check_output(['uptime', '-p']).decode('utf-8').strip("\n")
    time_pretty = re.search(r'up (.*)?', proc2)
    time_strings = [time_pretty.group(1), "(" + time.group(1) + ")"]
    time_stuff = " ".join(time_strings)
    yield from bot.coro_send_message(event.conv_id, time_stuff)


def get_status(players=False):
    url = 'https://fantasy.premierleague.com/a/leagues/standings/229216/h2h/'
    header = {'User-Agent': 'Mozilla/5.0'}
    r = urllib.request.Request(url=url, headers=header)
    page = urllib.request.urlopen(r)
    soup = BeautifulSoup(page.read(), "lxml")
    string = '.ism-main h2.ism-section-title, .ism-table--standings tr:nth-of-type(1) td:nth-of-type(1), .ism-table--standings tr:nth-of-type(1) td:nth-of-type(1) strong'
    data = soup.select(string)

    title = data[1].contents[0].strip()
    rank = data[2].contents[0].strip()
    teamName = data[3].contents[0].strip()
    return title
    return test
    return teamName


def ping():
    server = "209.95.56.13"
    proc = subprocess.check_output(['ping', '-c1', server])
    return ping == 0