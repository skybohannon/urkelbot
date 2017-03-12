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
import requests
import re
import subprocess
import json
import io
import os
import aiohttp
import csv
import urllib.parse
from bs4 import BeautifulSoup


def _initialize(bot):
    plugins.register_user_command(["uptime"])
    plugins.register_user_command(["fpl"])
    plugins.register_user_command(["ping"])

def uptime(bot, event, *args):
    proc1 = subprocess.check_output(['uptime']).decode('utf-8').strip("\n")
    time = re.search(r'up (.* days)?', proc1)
    proc2 = subprocess.check_output(['uptime', '-p']).decode('utf-8').strip("\n")
    time_pretty = re.search(r'up (.*)?', proc2)
    time_strings = [time_pretty.group(1), "(" + time.group(1) + ")"]
    time_stuff = " ".join(time_strings)
    yield from bot.coro_send_message(event.conv_id, time_stuff)

def fpl(bot, event, *args):
    url = 'http://www.fplstatistics.co.uk/Home/IndexWG'
    header = {'User-Agent': 'Mozilla/5.0'}

    r = urllib.request.Request(url=url, headers=header)
    page = urllib.request.urlopen(r)
    soup = BeautifulSoup(page.read(), "lxml")
    string = 'tbody tr:nth-of-type(1) td:nth-of-type(1), tbody tr:nth-of-type(1) td:nth-of-type(2), tbody tr:nth-of-type(1) td:nth-of-type(6), tbody tr:nth-of-type(1) td:nth-of-type(9) div'
    data = soup.select(string)

    playerName = data[0].contents[0].strip()
    playerTeam = data[1].contents[0].strip()
    playerPrice = data[2].contents[0].strip()
    playerTarget = data[3].contents[0].strip()

    fpl_strings = [playerName, playerTeam, playerPrice, playerTarget] 
    print(" ".join(fpl_strings))
    return "<br/>".join(fpl_strings)

    yield from bot.coro_send_message(event.conv_id, fpl_strings)

def ping(bot, event, *args):
    server = "209.95.56.13"
    try:
        proc = subprocess.check_output(['ping', '-c1', server])
        string = proc.decode('utf-8')
        ping = re.search(r'rtt min/avg/max/mdev = \d+\.\d+/(\d+\.\d+)/\d+\.\d+/', string)
        ping_stuff = ping.group(1)
        yield from bot.coro_send_message(event.conv.id_, server + ": " + ping_stuff)
    except subprocess.CalledProcessError:
        yield from bot.coro_send_message(event.conv.id_, "Ping command doesn't work right now")
